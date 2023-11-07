import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Label, StringVar, Toplevel
from tkinter import messagebox
from AlmaIntegral.Modelo.Bases_de_datos import DataBase
from AlmaIntegral.Modelo.Products import ManagementProduct
from AlmaIntegral.Modelo.Bases_de_datos import DataBase
from AlmaIntegral.Modelo.Products import ManagementProduct

class XD:
    def __init__(self, ):
        self.database = DataBase("../../assets/Inventory.db")
        self.products = ManagementProduct("../../assets/Inventory.db")

        self.window = None
        self.canvas = None

        self.code = None
        self.name = None
        self.price = None
        self.category = None
        self.brand = None
        self.quantity = None

        self.code_actual = None
        self.name_actual = None
        self.price_actual = None
        self.category_actual = None
        self.brand_actual = None
        self.quantity_actual = None

        self.txt_code = None
        self.txt_name = None
        self.txt_price = None
        self.txt_category = None
        self.txt_brand = None
        self.txt_quantity = None

        self.lbl_code = None
        self.lbl_name = None
        self.lbl_price = None
        self.lbl_category = None
        self.lbl_brand = None
        self.lbl_quantity = None

        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.button_4 = None

        self.table1 = None
        self.table2 = None

    def create_window(self):
        self.window = Tk()
        self.window.geometry("1050x600")
        self.window.configure(bg="#59A76E")

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#59A76E",
            height=800,
            width=1050,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            5.684341886080802e-14,
            33.99999999999997,
            1050.0,
            800.0,
            fill="#FFFFFF",
            outline="")

    def labels(self):
        self.lbl_quantity = Label(self.window, foreground="black", background="white", text="Quantity", font=8)
        self.lbl_quantity.place(x=60, y=160)
        self.lbl_name = Label(self.window, foreground="black", background="white", text="Name", font=8)
        self.lbl_name.place(x=60, y=500)
        self.lbl_price = Label(self.window, foreground="black", background="white", text="Price", font=8)
        self.lbl_price.place(x=280, y=500)
        self.lbl_category = Label(self.window, foreground="black", background="white", text="Category", font=8)
        self.lbl_category.place(x=480, y=500)
        self.lbl_brand = Label(self.window, foreground="black", background="white", text="Brand", font=8)
        self.lbl_brand.place(x=680, y=500)

    def entries(self):
        self.code = StringVar()
        self.name = StringVar()
        self.quantity = StringVar()
        self.price = StringVar()
        self.category = StringVar()
        self.brand = StringVar()
        self.txt_name = Entry(self.window, font=("Arial", 12), textvariable=self.name)
        self.txt_name.place(x=60, y=530)
        self.txt_quantity = Entry(self.window, font=("Arial", 12), textvariable=self.quantity)
        self.txt_quantity.place(x=140, y=160)
        self.txt_price = Entry(self.window, font=("Arial", 12), textvariable=self.price)
        self.txt_price.place(x=280, y=530)
        self.txt_category = Entry(self.window, font=("Arial", 12), textvariable=self.category)
        self.txt_category.place(x=480, y=530)
        self.txt_brand = Entry(self.window, font=("Arial", 12), textvariable=self.brand)
        self.txt_brand.place(x=680, y=530)

    def buttons(self):
        self.button_1 = Button(self.window, text="Add Quantity", relief="flat", background="#59A76E",
                               foreground="black", command=lambda: self.add(self.quantity))
        self.button_1.place(x=140, y=200, width=90, height=40)
        self.button_2 = Button(self.window, text="Back", relief="flat", background="#59A76E",
                               foreground="black")
        self.button_2.place(x=240, y=200, width=90, height=40)
        self.button_3 = Button(self.window, text="Modify", relief="flat", background="#59A76E",
                               foreground="black", command=self.modify)
        self.button_3.place(x=880, y=540, width=90, height=30)
        self.button_4 = Button(self.window, text="Delete", relief="flat", background="#59A76E",
                               foreground="black", command=lambda: self.delete(self.code))
        self.button_4.place(x=880, y=500, width=90, height=30)

    def modify(self):
        self.get_information()
        self.products.modify_product(self.code_actual, self.name_actual, self.price_actual, self.category_actual, self.brand_actual)
        messagebox.showinfo("Se ha actualizado exitosamente")
        self.db_table_inventories()
        self.db_table_products()

    def start_window(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def db_table_inventories(self):
        self.table1 = ttk.Treeview(self.window, columns=("1", "2", "3"), show="headings", height=6)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#59A76E", relief="flat", foreground="white")
        self.table1.heading("1", text="Code")
        self.table1.heading("2", text="Name")
        self.table1.heading("3", text="Quantity")

        self.table1.place(x=350, y=90)

        elements1 = self.database.return_all_elements("Inventories")
        for i in elements1:
            self.table1.insert("", "end", values=i)

        self.table1.bind("<Double 1>", self.get_row_table1)

    def get_row_table1(self, event):
        self.table1.identify_row(event.y)
        element = self.table1.item(self.table1.focus())
        q = element['values'][2]
        self.quantity.set(q)

    def db_table_products(self):
        self.table2 = ttk.Treeview(self.window, columns=("1", "2", "3", "4", "5"), show="headings", height=6)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#59A76E", relief="flat", foreground="white")
        self.table2.heading("1", text="Code")
        self.table2.heading("2", text="Name")
        self.table2.heading("3", text="Price")
        self.table2.heading("4", text="Category")
        self.table2.heading("5", text="Brand")

        self.table2.place(x=30, y=330)

        elements = self.database.return_all_elements("Products")
        for i in elements:
            self.table2.insert("", "end", values=i)

        self.table2.bind("<Double 1>", self.get_row_table2)

    def get_row_table2(self, event):
        self.table1.identify_row(event.y)
        element = self.table2.item(self.table2.focus())
        co = element['values'][0]
        n = element['values'][1]
        p = element['values'][2]
        c = element['values'][3]
        b = element['values'][4]
        self.code.set(co)
        self.name.set(n)
        self.price.set(p)
        self.category.set(c)
        self.brand.set(b)

    def get_information_code(self):
        if self.code.get():
            self.code_actual = self.code.get()

    def get_information_price(self):
        if self.price.get():
            self.price_actual = self.price.get()

    def get_information_category(self):
        if self.category.get():
            self.category_actual = self.category.get()

    def get_information_brand(self):
        if self.brand.get():
            self.brand_actual = self.brand.get()

    def get_information_add_quantity(self):
        if self.quantity.get():
            self.quantity_actual = self.quantity.get()

    def get_information_name(self):
        if self.name.get():
            self.name_actual = self.name.get()

    def get_information(self):
        self.get_information_code()
        self.get_information_name()
        self.get_information_price()
        self.get_information_category()
        self.get_information_brand()
        self.get_information_add_quantity()

    def start(self):
        self.create_window()
        self.create_canvas()
        self.labels()
        self.entries()
        self.buttons()
        self.db_table_inventories()
        self.db_table_products()
        self.start_window()


xd = XD()
xd.start()