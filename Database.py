import hashlib
import secrets

import psycopg2
from typing import List, Tuple, Union, Optional


class Database:
    def __init__(self, host: str, database: str, user: str, password: str, port: str = '5432') -> None:
        try:
            self.connection = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def close(self) -> None:
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str) -> bool:
        try:
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            return False

    def fetch_data(self, query: str) -> List[Tuple]:
        try:
            print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(f"Error fetching data: {e}")
            self.connection.rollback()
            return []

    def insert_data(self, table: str, columns: List[str], values: List[Union[str, int]]) -> bool:
        column_str = ', '.join(columns)
        value_str = ', '.join([str(value) for value in values])
        if 'id' not in columns or len(columns) == len(values):
            query = f"INSERT INTO {table} ({column_str}) VALUES ({value_str})"
        else:
            query = f"INSERT INTO {table} ({column_str}) VALUES (DEFAULT, {value_str})"
        return self.execute_query(query)

    def select_data(self, table: str, columns: Union[str, List[str]] = "*", condition: str = "") -> List[Tuple]:
        column_str = ", ".join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {column_str} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        return self.fetch_data(query)

    def update_data(self, table: str, column_value_pairs: dict, condition: str = "") -> bool:
        set_str = ', '.join([f"{column} = '{value}'" for column, value in column_value_pairs.items()])
        query = f"UPDATE {table} SET {set_str}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query)

    def delete_data(self, table: str, condition: str = "") -> bool:
        query = f"DELETE FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query)

    def get_table_data(self, table: str) -> Tuple[List[str], List[Tuple]]:
        query = f"SELECT * FROM {table}"
        result = self.fetch_data(query)
        if result:
            column_names = [desc[0] for desc in self.cursor.description]
            rows = result
            return column_names, rows
        return [], []

    def authenticate_user(self, login: str, password: str) -> bool:
        query = f"SELECT h_password, salt FROM useraccount WHERE login = '{login}'"
        result = self.execute_query(query)
        if result:
            row = self.cursor.fetchone()
            if row:
                stored_password = row[0]
                salt = row[1]
                hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
                return stored_password == hashed_password
        return False

    def create_user(self, login: str, password: str, role: str = 'default') -> bool:
        salt = secrets.token_hex(16)
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        query = f"INSERT INTO useraccount (login, h_password, salt,role) " \
                f"VALUES ('{login}', '{hashed_password}', '{salt}',{role})"
        return self.execute_query(query)

    def change_password(self, id: str, password: str) -> bool:
        salt = secrets.token_hex(16)
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        query = f"UPDATE useraccount SET h_password = '{hashed_password}', salt = '{salt}' WHERE id = '{id}'"
        return self.execute_query(query)

    def get_user_role(self, login: str) -> Optional[str]:
        query = f"SELECT r.lvl FROM role r INNER JOIN useraccount u ON r.id = u.role WHERE u.login = '{login}'"
        result = self.execute_query(query)
        if result:
            row = self.cursor.fetchone()
            if row:
                return row[0]
        return None

    def get_available_apartments(self):
        return self.fetch_data(
            "SELECT id FROM apartment WHERE id NOT IN (SELECT apartment FROM orders WHERE CURRENT_DATE BETWEEN check_in AND check_out)")

    def get_foreign_key(self, table):
        if table in self.execute_query("SELECT table_name FROM information_schema"):
            return self.select_data(table, "id")
