from AlmaIntegral.Modelo.Bases_de_datos import DataBase
import re


class User:
    def __init__(self, user_name: str, email: str, password: str, role: str):
        self.user_name: str = user_name
        self.email: str = email
        self.password: str = password
        self.role: str = role


class Employee(User):
    def __init__(self, user_name: str, email: str, password: str, role: str):
        super().__init__(user_name, email, password, role)


class Admin(User):
    def __init__(self, user_name: str, email: str, password: str, role: str):
        super().__init__(user_name, email, password, role)


class UserManagement:
    def __init__(self, address_connection):
        self.address_connection = address_connection

    def verify_user_exist(self, email: str) -> bool:
        db = DataBase(self.address_connection)
        if db.verify_user_exist_db(email):
            return True
        return False

    def verify_credential(self, email: str, password: str) -> bool:
        db = DataBase(self.address_connection)
        if db.verify_user_credential_db(email, password):
            return True
        return False

    def verify_rol(self, email: str):
        db = DataBase(self.address_connection)
        return db.verify_rol_db(email)

    @staticmethod
    def verify_email(email: str) -> bool:
        patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(patron, email):
            return True
        else:
            return False

    def save_register(self, name: str, email: str, password: str, rol: str):
        db = DataBase(self.address_connection)
        db.insert_rows_users(name, email, password, rol)


