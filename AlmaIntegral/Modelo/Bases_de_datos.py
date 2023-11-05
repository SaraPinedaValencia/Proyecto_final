import sqlite3 as sql


class DataBase:

    def __init__(self, address_connection):
        self.address_connection = address_connection

    def created_db(self):
        conn = sql.connect(self.address_connection)
        conn.commit()
        conn.close()

    def created_table_users(self):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(
            f"""CREATE TABLE Users (
                name text,
                email text primary key,
                password text,
                role text
            )""")
        conn.commit()
        conn.close()

    def created_table_products(self):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(
            f"""CREATE TABLE Products (
                code TEXT PRIMARY KEY,
                name TEXT PRIMARY KEY,
                price REAL,
                category TEXT,
                brand TEXT
            )""")
        conn.commit()
        conn.close()

    def created_table_inventories(self):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(
            f"""CREATE TABLE Inventories (
                code TEXT,
                name TEXT,
                quantity INTEGER,
                FOREIGN KEY (code, name) REFERENCES Products (code, name)
            )""")
        conn.commit()
        conn.close()

    def insert_rows_users(self, name: str, email: str, password: str, rol: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO Users VALUES ('{name}', '{email}', '{password}', '{rol}')""")
        conn.commit()
        conn.close()

    def insert_rows_products(self, code: str, name: str, price: float, category: str, brand: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO products VALUES ('{code}', '{name}', '{price}', '{category}', '{brand}')""")
        conn.commit()
        conn.close()

    def insert_rows_inventories(self, code: str, name: str, quantity: int):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO Inventories VALUES ('{code}', '{name}', '{quantity}')""")
        conn.commit()
        conn.close()

    def verify_user_credential_db(self, email: str, password: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE email = '{email}' AND password = '{password}';")
        result1 = cursor.fetchall()
        conn.commit()
        conn.close()
        return result1

    def verify_user_exist_db(self, email: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE email = '{email}'")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    def verify_code_exist_db(self, code: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Products WHERE code = '{code}'")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    def verify_name_exist_db(self, name: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Products WHERE code = '{name}'")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    def return_all_elements(self, table_name: str):
        conn = sql.connect(self.address_connection)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result


'''if __name__ == "__main__":
    db = DataBase("../assets/Inventory.db")
    db.insert_rows_inventories("0000", "Yogurt Griego Natural 1L", 0)'''

