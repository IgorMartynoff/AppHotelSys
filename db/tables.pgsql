-- 1.Passport
CREATE TABLE
    passport (
        id serial PRIMARY KEY,
        country varchar(100) DEFAULT NULL,
        type varchar(50) DEFAULT NULL,
        series varchar(10) DEFAULT NULL,
        number varchar(10) DEFAULT NULL,
        gender varchar(10) DEFAULT NULL,
        d_birth date DEFAULT NULL,
        d_issue date DEFAULT NULL,
        by_issue varchar(100) DEFAULT NULL
    );

-- 2.Role
CREATE TABLE
    role (
        id serial PRIMARY KEY,
        title varchar(50) NOT NULL,
        lvl integer NOT NULL
    );

-- 3.UserAccount
CREATE TABLE
    useraccount (
        id serial PRIMARY KEY,
        login varchar(50) NOT NULL,
        h_password varchar(100) NOT NULL,
        salt varchar(100) NOT NULL,
        role integer REFERENCES role (id) ON DELETE SET NULL
    );

-- 4.Discount
CREATE TABLE
    discount (
        id serial PRIMARY KEY,
        title varchar(100) DEFAULT NULL,
        discount double precision DEFAULT NULL,
        reason varchar(100) DEFAULT NULL
    );

-- 5.DataPersonal
CREATE TABLE
    datapersonal (
        id serial PRIMARY KEY,
        f_name varchar(100) DEFAULT NULL,
        m_name varchar(100) DEFAULT NULL,
        l_name varchar(100) DEFAULT NULL,
        n_phone varchar(50) DEFAULT NULL,
        passport integer REFERENCES passport (id) ON DELETE SET NULL
    );

-- 6.Guest
CREATE TABLE
    guest (
        id serial PRIMARY KEY,
        discount integer REFERENCES discount (id) ON DELETE SET NULL,
        datapersonal integer REFERENCES datapersonal (id) ON DELETE SET NULL
    );

-- 7.Typeapart
CREATE TABLE
    typeapart (
        id serial PRIMARY KEY,
        title varchar(100) NOT NULL
    );

-- 8.Apartment
CREATE TABLE
    apartment (
        id serial PRIMARY KEY,
        title varchar(100) DEFAULT NULL,
        cnt_bed integer DEFAULT 1,
        price integer DEFAULT 1000,
        typeapart integer REFERENCES typeapart (id) ON DELETE SET NULL
    );

-- 9.Staff
CREATE TABLE
    staff (
        id serial PRIMARY KEY,
        w_hours integer DEFAULT NULL,
        salary integer DEFAULT NULL,
        address varchar(100) DEFAULT NULL,
        datapersonal integer REFERENCES datapersonal (id) ON DELETE SET NULL,
        useraccount integer REFERENCES useraccount (id) ON DELETE SET NULL
    );

-- 10.Order
CREATE TABLE
    orders (
        id serial PRIMARY KEY,
        price integer,
        check_in date DEFAULT current_date,
        check_out date NOT NULL,
        guest integer REFERENCES guest (id) ON DELETE SET NULL,
        apartment integer REFERENCES apartment (id) ON DELETE SET NULL
    );

-- Create a trigger function to calculate the default value for the "check" column
CREATE OR REPLACE FUNCTION calculate_price() RETURNS TRIGGER AS $$
DECLARE
    total_days integer;
    apartment_price integer;
    discount_amount numeric;
BEGIN
    total_days := NEW.check_out - NEW.check_in;
    SELECT price INTO apartment_price FROM apartment WHERE id = NEW.apartment;
    SELECT COALESCE(discount, 0) INTO discount_amount FROM 
        discount WHERE id = (SELECT discount FROM guest WHERE id = NEW.guest);
    IF discount_amount IS NULL THEN
        discount_amount := 0;
    END IF;
    NEW.price := total_days * apartment_price * (1 - discount_amount)::numeric::integer;
    IF NEW.price IS NULL THEN
        NEW.price := apartment_price;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to invoke the trigger function before inserting a new row
CREATE TRIGGER calculate_order_price_trigger
BEFORE INSERT ON orders
FOR EACH ROW
EXECUTE FUNCTION calculate_price();


-- Create a trigger to invoke the trigger function before inserting a new row
CREATE TRIGGER calculate_check_trigger BEFORE INSERT ON orders FOR EACH ROW
EXECUTE FUNCTION calculate_check_amount ();

-- 11.Logs
CREATE TYPE ACTION_TYPE AS ENUM('update', 'delete');

CREATE TABLE
    logs (
        id SERIAL PRIMARY KEY,
        user_ VARCHAR(100),
        time_ TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        table_ VARCHAR(50),
        data_ TEXT,
        action_ ACTION_TYPE DEFAULT 'delete'
    );

CREATE INDEX logs_user_idx ON logs (user_);

CREATE INDEX logs_table_name_idx ON logs (table_);

CREATE INDEX logs_date_idx ON logs (date_);