-- 1.Create view guest_d
CREATE OR REPLACE VIEW guest_d AS
SELECT
    g.id AS id,
    dp.f_name,
    dp.m_name,
    dp.l_name,
    dp.n_phone,
    p.country,
    p.type,
    p.series,
    p.number,
    p.gender,
    p.d_birth,
    p.d_issue,
    p.by_issue,
    d.id AS discount
FROM
    guest g
JOIN
    datapersonal dp ON g.datapersonal = dp.id
JOIN
    passport p ON dp.passport = p.id
LEFT JOIN
    discount d ON g.discount = d.id;
-- 1.1 Create Function for rule INSERT
CREATE OR REPLACE FUNCTION insert_guest_d() RETURNS TRIGGER AS $$
DECLARE
    passport_id INTEGER;
    datapersonal_id INTEGER;
BEGIN
    INSERT INTO passport (country, type, series, number, gender, d_birth, d_issue, by_issue)
    VALUES (NEW.country, NEW.type, NEW.series, NEW.number, NEW.gender, NEW.d_birth, NEW.d_issue, NEW.by_issue)
    RETURNING id INTO passport_id;

    INSERT INTO datapersonal (f_name, m_name, l_name, n_phone, passport)
    VALUES (NEW.f_name, NEW.m_name, NEW.l_name, NEW.n_phone, passport_id)
    RETURNING id INTO datapersonal_id;

    INSERT INTO guest (datapersonal, discount)
    VALUES (datapersonal_id, COALESCE(NEW.discount, 1));

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- 1.1 Create the trigger
CREATE TRIGGER insert_guest_d_trigger
INSTEAD OF INSERT ON guest_d
FOR EACH ROW
EXECUTE FUNCTION insert_guest_d();


--1.2 Create Function for rule DELETE
CREATE OR REPLACE FUNCTION delete_guest_d() RETURNS TRIGGER AS $$
DECLARE
    datapersonal_id INTEGER;
BEGIN
    SELECT datapersonal INTO datapersonal_id FROM guest WHERE id = OLD.id;
    DELETE FROM guest WHERE id = OLD.id;
    DELETE FROM datapersonal WHERE id = datapersonal_id;
    DELETE FROM passport WHERE id = 
        (SELECT passport FROM datapersonal WHERE id = datapersonal_id);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

--1.2 Create the trigger
CREATE TRIGGER delete_guest_d_trigger
INSTEAD OF DELETE ON guest_d
FOR EACH ROW
EXECUTE FUNCTION delete_guest_d();


-- 1.3 Create Function for rule UPDATE
CREATE OR REPLACE FUNCTION update_guest_d() RETURNS TRIGGER AS $$
DECLARE
    datapersonal_id INTEGER;
BEGIN
    SELECT datapersonal INTO datapersonal_id
    FROM guest
    WHERE id = NEW.id;

    UPDATE passport
    SET country = NEW.country,
        type = NEW.type,
        series = NEW.series,
        number = NEW.number,
        gender = NEW.gender,
        d_birth = NEW.d_birth,
        d_issue = NEW.d_issue,
        by_issue = NEW.by_issue
    WHERE id = (SELECT passport FROM datapersonal WHERE id = datapersonal_id);

    UPDATE datapersonal
    SET f_name = NEW.f_name,
        m_name = NEW.m_name,
        l_name = NEW.l_name,
        n_phone = NEW.n_phone
    WHERE id = datapersonal_id;

    UPDATE guest
    SET discount = COALESCE(NEW.discount, 1)
    WHERE id = NEW.id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


--1.3 Create the trigger
CREATE TRIGGER update_guest_d_trigger
INSTEAD OF UPDATE ON guest_d
FOR EACH ROW
EXECUTE FUNCTION update_guest_d();


-- 2. Create view staff_d

CREATE OR replace VIEW staff_d AS
SELECT
    s.id AS id,
    s.w_hours,
    s.salary,
    s.address,
    s.useraccount,
    dp.f_name,
    dp.m_name,
    dp.l_name,
    dp.n_phone,
    p.country,
    p.type,
    p.series,
    p.number,
    p.gender,
    p.d_birth,
    p.d_issue,
    p.by_issue
FROM
    staff s
JOIN
    datapersonal dp ON s.datapersonal = dp.id
JOIN
    passport p ON dp.passport = p.id;
-- 2.1 Create Function for rule INSERT
CREATE OR REPLACE FUNCTION insert_staff_d() RETURNS TRIGGER AS $$
DECLARE
    passport_id INTEGER;
    datapersonal_id INTEGER;
    staff_useraccount INTEGER;
BEGIN
    INSERT INTO passport (country, type, series, number, gender, d_birth, d_issue, by_issue)
    VALUES (NEW.country, NEW.type, NEW.series, NEW.number, NEW.gender, NEW.d_birth, NEW.d_issue, NEW.by_issue)
    RETURNING id INTO passport_id;

    INSERT INTO datapersonal (f_name, m_name, l_name, n_phone, passport)
    VALUES (NEW.f_name, NEW.m_name, NEW.l_name, NEW.n_phone, passport_id)
    RETURNING id INTO datapersonal_id;

    IF NEW.useraccount IS NOT NULL THEN
        INSERT INTO staff (w_hours, salary, address, datapersonal, useraccount)
        VALUES (NEW.w_hours, NEW.salary, NEW.address, datapersonal_id, NEW.useraccount)
        RETURNING id INTO staff_useraccount;
    ELSE
        INSERT INTO staff (w_hours, salary, address, datapersonal)
        VALUES (NEW.w_hours, NEW.salary, NEW.address, datapersonal_id)
        RETURNING id INTO staff_useraccount;
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
-- 2.1Create the trigger
CREATE TRIGGER insert_staff_d_trigger
INSTEAD OF INSERT ON staff_d
FOR EACH ROW
EXECUTE FUNCTION insert_staff_d();


-- 2.2 Create Function for rule DELETE
CREATE OR REPLACE FUNCTION delete_staff_d() RETURNS TRIGGER AS $$
DECLARE
    datapersonal_id INTEGER;
BEGIN
    SELECT datapersonal INTO datapersonal_id
    FROM staff
    WHERE id = OLD.id;

    DELETE FROM staff WHERE id = OLD.id;
    DELETE FROM datapersonal WHERE id = datapersonal_id;
    DELETE FROM passport WHERE id = (SELECT passport FROM datapersonal WHERE id = datapersonal_id);

    -- Check if the staff record had an associated useraccount and delete it
    IF EXISTS (SELECT 1 FROM useraccount WHERE id = OLD.id_useraccount) THEN
        DELETE FROM useraccount WHERE id = OLD.id_useraccount;
    END IF;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER delete_staff_d_trigger
INSTEAD OF DELETE ON staff_d
FOR EACH ROW
EXECUTE FUNCTION delete_staff_d();


-- 2.3 Create Function for rule UPDATE
CREATE OR REPLACE FUNCTION update_staff_d() RETURNS TRIGGER AS $$
BEGIN
    UPDATE passport
    SET country = NEW.country,
        type = NEW.type,
        series = NEW.series,
        number = NEW.number,
        gender = NEW.gender,
        d_birth = NEW.d_birth,
        d_issue = NEW.d_issue,
        by_issue = NEW.by_issue
    WHERE id = (
        SELECT p.id
        FROM staff s
        JOIN datapersonal dp ON s.datapersonal = dp.id
        JOIN passport p ON dp.passport = p.id
        WHERE s.id = NEW.id
    );

    UPDATE datapersonal
    SET f_name = NEW.f_name,
        m_name = NEW.m_name,
        l_name = NEW.l_name,
        n_phone = NEW.n_phone
    WHERE id = (
        SELECT dp.id
        FROM staff s
        JOIN datapersonal dp ON s.datapersonal = dp.id
        WHERE s.id = NEW.id
    );

    UPDATE staff
    SET w_hours = NEW.w_hours,
        salary = NEW.salary,
        address = NEW.address,
        useraccount = NEW.id_useraccount
    WHERE id = NEW.id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 2.3 Create the trigger
CREATE TRIGGER update_staff_d_trigger
INSTEAD OF UPDATE ON staff_d
FOR EACH ROW
EXECUTE FUNCTION update_staff_d();


--3 Create the view apartment_d
CREATE OR REPLACE VIEW apartment_d AS
SELECT
    a.title,
    a.id,
    a.cnt_bed,
    a.price,
    COALESCE(t.title, 'Стандартная') AS typeapart_t
FROM
    apartment a
LEFT JOIN
    typeapart t ON a.typeapart = t.id;

--3.1 Create the trigger function for inserting into the view
CREATE OR REPLACE FUNCTION insert_apartment_d() RETURNS TRIGGER AS $$
DECLARE
    typeapart_id INTEGER;
BEGIN
    -- Check if the provided type_title already exists in typeapart
    SELECT id INTO typeapart_id FROM typeapart WHERE title = NEW.typeapart_t;

    -- If the type_title doesn't exist, insert it into typeapart
    IF typeapart_id IS NULL THEN
        INSERT INTO typeapart (title) VALUES (NEW.typeapart_t) RETURNING id INTO typeapart_id;
    END IF;

    -- Insert the apartment record into the apartment table
    INSERT INTO apartment (title, cnt_bed, price, typeapart)
    VALUES (NEW.title, NEW.cnt_bed, NEW.price, typeapart_id);

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

--3.1 Create the trigger for inserting into the view
CREATE TRIGGER insert_apartment_d_trigger
INSTEAD OF INSERT ON apartment_d
FOR EACH ROW
EXECUTE FUNCTION insert_apartment_d();

-- 3.2 Create the trigger function for DELETE
CREATE OR REPLACE FUNCTION delete_apartment_d() RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM apartment WHERE id = OLD.id;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- 3.2 Create the trigger for DELETE
CREATE TRIGGER delete_apartment_d_trigger
INSTEAD OF DELETE ON apartment_d
FOR EACH ROW
EXECUTE FUNCTION delete_apartment_d();


-- 3.3 Create the trigger function for UPDATE
CREATE OR REPLACE FUNCTION update_apartment_d() RETURNS TRIGGER AS $$
BEGIN
    -- Update the corresponding apartment record in the apartment table
    UPDATE apartment
    SET title = NEW.title,
        cnt_bed = NEW.cnt_bed,
        price = NEW.price,
        typeapart = (SELECT id FROM typeapart WHERE title = NEW.typeapart_t)
    WHERE id = NEW.id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 3.3 Create the trigger for UPDATE
CREATE TRIGGER update_apartment_d_trigger
INSTEAD OF UPDATE ON apartment_d
FOR EACH ROW
EXECUTE FUNCTION update_apartment_d();






