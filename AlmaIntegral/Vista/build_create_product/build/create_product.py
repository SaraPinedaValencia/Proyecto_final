import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
from AlmaIntegral.Modelo.Products import ManagementProduct, InventoriesManagement

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class CreateProduct:

    def __init__(self, ventana_anterior):
        self.inventories_management = InventoriesManagement("../assets/Inventory.db")
        self.products_management = ManagementProduct("../assets/Inventory.db")
        self.ventana_anterior3 = ventana_anterior

        self.window = None
        self.canvas = None

        self.button_image_1 = None
        self.button_image_2 = None

        self.entry_image_1 = None
        self.entry_image_2 = None
        self.entry_image_3 = None
        self.entry_image_4 = None
        self.entry_image_5 = None

        self.code_data = None
        self.name_data = None
        self.price_data = None
        self.category_data = None
        self.brand_data = None

        self.code_current = None
        self.name_current = None
        self.price_current = None
        self.category_current = None
        self.brand_current = None

        self.image_image_1 = None
        self.image_image_2 = None
        self.image_image_3 = None
        self.image_image_4 = None
        self.image_image_5 = None
        self.image_image_6 = None
        self.image_image_7 = None
        self.image_image_8 = None
        self.image_image_9 = None

    def create_window(self):
        self.window = Tk()
        self.window.geometry("360x800")
        self.window.configure(bg="#58A76E")

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#58A76E",
            height=800,
            width=360,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            360.0,
            719.0,
            fill="#FFFFFF",
            outline="")

    def button_back_create_product(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_menu,
            relief="flat"
        )
        button_1.place(
            x=111.0,
            y=669.0,
            width=138.0,
            height=50.0
        )

    def back_to_menu(self):
        self.window.destroy()
        self.ventana_anterior3.start_menu()

    def button_create_product(self):
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
            x=24.0,
            y=578.0,
            width=312.0,
            height=78.0
        )

    def brand(self):
        self.canvas.create_rectangle(
            47.0,
            537.0,
            314.0,
            538.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            162.0,
            543.0,
            anchor="nw",
            text="BRAND",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            196.5,
            520.5,
            image=self.entry_image_1
        )
        self.brand_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.brand_data.place(
            x=79.0,
            y=510.0,
            width=235.0,
            height=19.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            60.78125,
            522.34375,
            image=self.image_image_1
        )

    def category(self):
        self.canvas.create_rectangle(
            46.0,
            375.0,
            313.0,
            376.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            150.0,
            460.0,
            anchor="nw",
            text="CATEGORY",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            195.0,
            440.5,
            image=self.entry_image_2
        )
        self.category_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.category_data.place(
            x=77.0,
            y=430.0,
            width=236.0,
            height=19.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            60.0,
            442.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            59.0,
            431.0,
            image=self.image_image_3
        )

    def price(self):
        self.canvas.create_rectangle(
            46.0,
            455.0,
            313.0,
            456.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            160.0,
            377.0,
            anchor="nw",
            text="PRICE",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            193.0,
            361.0,
            image=self.entry_image_3
        )
        self.price_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.price_data.place(
            x=73.0,
            y=350.0,
            width=240.0,
            height=20.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            60.876949310302734,
            361.875,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            64.63636779785156,
            356.1666564941406,
            image=self.image_image_5
        )

    def name(self):
        self.canvas.create_text(
            160.0,
            298.0,
            anchor="nw",
            text="NAME",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            46.0,
            297.0,
            313.0,
            298.0,
            fill="#000000",
            outline="")

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            194.0,
            278.0,
            image=self.entry_image_4
        )
        self.name_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.name_data.place(
            x=75.0,
            y=267.0,
            width=238.0,
            height=20.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            58.75,
            277.75,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            58.663326263427734,
            275.3778991699219,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            58.828125,
            283.2134704589844,
            image=self.image_image_8
        )

    def code(self):
        self.canvas.create_text(
            162.0,
            220.0,
            anchor="nw",
            text="CODE",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            46.0,
            215.0,
            313.0,
            216.0,
            fill="#000000",
            outline="")

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            193.0,
            200.0,
            image=self.entry_image_5
        )
        self.code_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.code_data.place(
            x=73.0,
            y=188.0,
            width=240.0,
            height=22.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = self.canvas.create_image(
            58.0,
            200.0,
            image=self.image_image_9
        )

    def logo(self):
        self.canvas.create_text(
            91.0,
            115.0,
            anchor="nw",
            text="Create product",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

    def start_window(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def get_information_code(self):
        if self.code_data.get():
            self.code_current = self.code_data.get()
        else:
            messagebox.showerror("Error", "El campo del code está vacío")

    def get_information_name(self):
        if self.name_data.get():
            self.name_current = self.name_data.get()
        else:
            messagebox.showerror("Error", "El campo del name está vacío")

    def get_information_price(self):
        if self.price_data.get():
            self.price_current = self.price_data.get()
        else:
            messagebox.showerror("Error", "El campo del price está vacío")

    def get_information_category(self):
        if self.category_data.get():
            self.category_current = self.category_data.get()
        else:
            messagebox.showerror("Error", "El campo del category está vacío")

    def get_information_brand(self):
        if self.brand_data.get():
            self.brand_current = self.brand_data.get()
        else:
            messagebox.showerror("Error", "El campo del brand está vacío")

    def get_information(self):
        self.get_information_code()
        self.get_information_name()
        self.get_information_price()
        self.get_information_category()
        self.get_information_brand()
        if not self.products_management.verify_code_exist(self.code_current):
            if not self.products_management.verify_name_exist(self.name_current):
                self.products_management.save_register_product(self.code_current, self.name_current, self.price_current,
                                                               self.category_current, self.brand_current)
                self.inventories_management.save_register_inventory(self.code_current, self.name_current, 0)
            else:
                messagebox.showerror("Error", "El nombre ya existe, intente con otro")
        else:
            messagebox.showerror("Error", "Ese producto ya se encuentra registrado")

        print(self.code_current, self.name_current, self.price_current, self.category_current, self.brand_current)

    def start_create_product(self):
        self.create_window()
        self.create_canvas()
        self.button_back_create_product()
        self.button_create_product()
        self.brand()
        self.category()
        self.price()
        self.name()
        self.code()
        self.logo()
        self.start_window()


'''ventana = CreateProduct()
ventana.start_create_product()'''
