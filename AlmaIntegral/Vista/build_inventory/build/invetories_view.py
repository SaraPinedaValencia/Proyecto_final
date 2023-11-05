import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import messagebox
from AlmaIntegral.Modelo.Bases_de_datos import DataBase

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Inventory:
    def __init__(self):
        self.window = None
        self.canvas = None
        self.canvas_2 = None
        self.table = None

        self.database = DataBase("../../../assets/Inventory.db")

        self.button_image_1 = None
        self.button_image_2 = None
        self.button_image_3 = None
        self.button_image_4 = None
        self.button_image_5 = None

        self.entry_image_1 = None
        self.entry_image_2 = None
        self.entry_image_3 = None
        self.entry_image_4 = None
        self.entry_image_5 = None
        self.entry_image_6 = None

        self.image_image_1 = None
        self.image_image_2 = None
        self.image_image_3 = None
        self.image_image_4 = None
        self.image_image_5 = None
        self.image_image_6 = None
        self.image_image_7 = None
        self.image_image_8 = None
        self.image_image_9 = None
        self.image_image_10 = None

        self.add_quantity_data = None
        self.brand_data = None
        self.category_data = None
        self.price_data = None
        self.name_data = None
        self.filter_data = None

        self.filter_current = None
        self.name_current = None
        self.price_current = None
        self.category_current = None
        self.brand_current = None
        self.add_quantity_current = None

    def create_window(self):
        self.window = Tk()
        self.window.geometry("1000x800")
        self.window.configure(bg="#59A76E")

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#59A76E",
            height=800,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            5.684341886080802e-14,
            33.99999999999997,
            1000.0,
            800.0,
            fill="#FFFFFF",
            outline="")

        self.canvas_2 = Canvas(
            self.window,
            bg="#FFFFFF",
            height=800,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas_2.place(x=0, y=440)

    def db_table(self):
        self.table = ttk.Treeview(self.canvas_2, columns=("1", "2", "3"), show="headings", height=8)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#59A76E", relief="flat", foreground="white")
        self.table.heading("1", text="Code")
        self.table.heading("2", text="Name")
        self.table.heading("3", text="Quantity")

        self.table.place(x=200, y=0)

        elements = self.database.return_all_elements("Inventories")
        for i in elements:
            self.table.insert("", "end", values=i)

    def button_add_quantity(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        button_1.place(
            x=647.0,
            y=259.0,
            width=275.0,
            height=75.0
        )

    def button_back(self):
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        button_2.place(
            x=647.0,
            y=334.0,
            width=275.0,
            height=75.0
        )

    def button_delete(self):
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        button_3.place(
            x=647.0,
            y=183.99999999999997,
            width=275.0,
            height=75.0
        )

    def button_modify(self):
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        button_4.place(
            x=647.0,
            y=108.99999999999997,
            width=275.0,
            height=75.0
        )

    def button_filter(self):
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        button_5.place(
            x=647.0,
            y=33.99999999999997,
            width=275.0,
            height=75.0
        )

    def add_quantity_inventory(self):
        self.canvas.create_text(
            308.99999999999994,
            393.0526428222656,
            anchor="nw",
            text="ADD QUANTITY",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            185.99999999999994,
            386.52630615234375,
            587.0,
            387.52630615234375,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            386.99999999999994,
            367.7894744873047,
            image=self.entry_image_1
        )
        self.add_quantity_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.add_quantity_data.place(
            x=196.99999999999994,
            y=352.0,
            width=380.0,
            height=29.578948974609375
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            126.99999999999994,
            367.0,
            image=self.image_image_1
        )

    def brand_inventory(self):
        self.canvas.create_text(
            351.99999999999994,
            321.0526428222656,
            anchor="nw",
            text="BRAND",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            186.99999999999994,
            316.1052551269531,
            588.0,
            317.1052551269531,
            fill="#000000",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            387.99999999999994,
            295.7894744873047,
            image=self.entry_image_2
        )
        self.brand_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.brand_data.place(
            x=197.99999999999994,
            y=280.0,
            width=380.0,
            height=29.578948974609375
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            126.99999999999994,
            295.0,
            image=self.image_image_2
        )

    def category_inventory(self):
        self.canvas.create_text(
            329.99999999999994,
            261.22222900390625,
            anchor="nw",
            text="CATEGORY",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            185.99999999999994,
            251.33332824707028,
            587.0,
            252.33332824707028,
            fill="#000000",
            outline="")

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            386.99999999999994,
            233.81481170654294,
            image=self.entry_image_3
        )
        self.category_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.category_data.place(
            x=196.99999999999994,
            y=218.99999999999997,
            width=380.0,
            height=27.629623413085938
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            126.99999999999994,
            238.8157043457031,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            125.8461303710937,
            223.99999999999997,
            image=self.image_image_4
        )

    def price_inventory(self):
        self.canvas.create_text(
            355.99999999999994,
            200.05262756347653,
            anchor="nw",
            text="PRICE",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            185.99999999999994,
            192.7368469238281,
            587.0,
            193.7368469238281,
            fill="#000000",
            outline="")

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            386.99999999999994,
            174.78947448730466,
            image=self.entry_image_4
        )
        self.price_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.price_data.place(
            x=196.99999999999994,
            y=158.99999999999997,
            width=380.0,
            height=29.578948974609375
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            126.99999999999994,
            173.99999999999997,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            137.95324707031244,
            164.45343017578122,
            image=self.image_image_6
        )

    def name_inventory(self):
        self.canvas.create_text(
            355.99999999999994,
            139.53845214843747,
            anchor="nw",
            text="NAME",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            185.99999999999994,
            132.38461303710935,
            587.0,
            133.38461303710935,
            fill="#000000",
            outline="")

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            386.99999999999994,
            113.38461303710935,
            image=self.entry_image_5
        )
        self.name_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.name_data.place(
            x=196.99999999999994,
            y=97.99999999999997,
            width=380.0,
            height=28.76922607421875
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            126.99999999999994,
            112.99999999999997,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            126.40147399902338,
            110.69627380371091,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = self.canvas.create_image(
            126.91667175292963,
            120.14662933349607,
            image=self.image_image_9
        )

    def search_inventory(self):
        self.canvas.create_text(
            344.99999999999994,
            75.71830749511716,
            anchor="nw",
            text="SEARCH",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_rectangle(
            184.99999999999994,
            71.33802795410153,
            586.0,
            72.33802795410153,
            fill="#000000",
            outline="")

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            385.99999999999994,
            52.90140914916989,
            image=self.entry_image_6
        )
        self.filter_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.filter_data.place(
            x=195.99999999999994,
            y=35.99999999999997,
            width=380.0,
            height=31.802818298339844
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        image_10 = self.canvas.create_image(
            126.99999999999994,
            51.99999999999997,
            image=self.image_image_10
        )

    def logo_inventory(self):
        self.canvas.create_text(
            399.99999999999994,
            2.842170943040401e-14,
            anchor="nw",
            text="INVENTORY",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

    def start_window(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def get_information_filter(self):
        if self.filter_data.get():
            self.filter_current = self.filter_data.get()
        else:
            messagebox.showerror("Error", "El campo del code está vacío")

    def get_information_name(self):
        if self.name_data.get():
            self.name_current = self.name_data.get()

    def get_information_price(self):
        if self.price_data.get():
            self.price_current = self.price_data.get()

    def get_information_category(self):
        if self.category_data.get():
            self.category_current = self.category_data.get()

    def get_information_brand(self):
        if self.brand_data.get():
            self.brand_current = self.brand_data.get()

    def get_information_add_quantity(self):
        if self.add_quantity_data.get():
            self.add_quantity_current = self.add_quantity_data.get()

    def get_information(self):
        self.get_information_filter()
        self.get_information_name()
        self.get_information_price()
        self.get_information_category()
        self.get_information_brand()
        self.get_information_add_quantity()

        print(self.filter_current, self.name_current, self.price_current, self.category_current, self.brand_current, self.add_quantity_current)

    def start_inventory(self):
        inventory = Inventory()
        inventory.create_window()
        inventory.create_canvas()
        inventory.db_table()
        inventory.button_add_quantity()
        inventory.button_back()
        inventory.button_delete()
        inventory.button_modify()
        inventory.button_filter()
        inventory.add_quantity_inventory()
        inventory.brand_inventory()
        inventory.category_inventory()
        inventory.price_inventory()
        inventory.name_inventory()
        inventory.search_inventory()
        inventory.logo_inventory()
        inventory.start_window()


ventana = Inventory()
ventana.start_inventory()
