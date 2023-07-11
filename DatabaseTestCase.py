import unittest
from Database import Database
import os
from dotenv import load_dotenv


class DatabaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.database = Database(
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST")
        )
        cls.create_test_table()

    def test_authenticate_user(self):
        self.assertTrue(self.database.authenticate_user("adm", "adm"))
        self.assertFalse(self.database.authenticate_user("user", "admin"))
        self.assertFalse(self.database.authenticate_user("admin", "password"))
        self.assertFalse(self.database.authenticate_user("132", "123"))

    def test_get_user_role(self):
        self.assertEqual(self.database.get_user_role("adm"), 1)
        self.assertIsNone(self.database.get_user_role("user"))
        self.assertEqual(self.database.get_user_role("123"), 2)

    def test_select_data(self):
        result = self.database.select_data("orders")
        self.assertNotEqual(result, [])
        result = self.database.select_data("non_existing_table")
        self.assertEqual(result, [])
        result = self.database.select_data("123")
        self.assertEqual(result, [])

    def test_insert_data(self):
        table = "test_table"
        columns = ["name"]
        values = ["'John'"]
        self.assertTrue(self.database.insert_data(table, columns, values))
        result = self.database.select_data(table)
        self.assertIn(''.join(values).replace("'", "").replace('"', "'"), result[-1])

    def test_update_data(self):
        table = "test_table"
        condition = "id = 1"
        column_value_pairs = {"name": "Jane"}
        self.assertTrue(self.database.update_data(table, column_value_pairs, condition))
        result = self.database.select_data(table, condition=condition)
        print(result)
        self.assertEqual(result[0][1], "Jane")

    def test_delete_data(self):
        table = "test_table"
        condition = "id = 1"
        self.assertTrue(self.database.delete_data(table, condition))
        result = self.database.select_data(table, condition=condition)
        self.assertEqual(result, [])

    @classmethod
    def tearDownClass(cls):
        cls.database.execute_query("DROP TABLE IF EXISTS test_table")

    @classmethod
    def create_test_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        )
        """
        cls.database.execute_query(query)


if __name__ == '__main__':
    unittest.main()
