from AlmaIntegral.Modelo.Bases_de_datos import DataBase


class ManagementProduct:
    def __init__(self, address_connection):
        self.address_connection = address_connection

    def verify_code_exist(self, code: str) -> bool:
        db = DataBase(self.address_connection)
        if db.verify_code_exist_db(code):
            return True
        return False

    def verify_name_exist(self, name: str) -> bool:
        db = DataBase(self.address_connection)
        if db.verify_name_exist_db(name):
            return True
        return False

    def save_register_product(self, code: str, name: str, price: float, category: str, brand: str):
        db = DataBase(self.address_connection)
        db.insert_rows_products(code, name, price, category, brand)

    def modify_product(self, code: str, name: str, price: float, category: str, brand: str):
        db = DataBase(self.address_connection)
        db.up_date_item(code, name, price, category, brand)


class InventoriesManagement:
    def __init__(self, address_connection):
        self.address_connection = address_connection

    def save_register_inventory(self, code: str, name: str, quantity: int):
        db = DataBase(self.address_connection)
        db.insert_rows_inventories(code, name, quantity)
