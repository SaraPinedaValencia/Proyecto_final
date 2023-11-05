import os
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from AlmaIntegral.Vista.build_register.register import Register
from AlmaIntegral.Vista.build_create_product.build.create_product import CreateProduct
from AlmaIntegral.Vista.build_inventory.build.invetories_view import Inventory

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Menu:
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.register = Register(self)
        self.create = CreateProduct(self)
        self.inventories = Inventory()
        self.window = None
        self.canvas = None

        self.button_image_1 = None
        self.button_image_2 = None
        self.button_image_3 = None
        self.button_image_4 = None

        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.button_4 = None

        self.image_image_1 = None
        self.image_image_2 = None

        self.image_1 = None
        self.image_2 = None

    def create_window(self):
        self.window = Tk()
        self.window.geometry("360x800")
        self.window.configure(bg="#58A76E")

    def set_up_canvas(self):
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
            61.999999999999886,
            360.0,
            799.9999999999999,
            fill="#FFFFFF",
            outline="")

    def button_sign_off(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back_to_login,
            relief="flat"
        )
        self.button_1.place(
            x=9.0,
            y=398.9999999999999,
            width=336.0,
            height=64.0
        )

    def back_to_login(self):
        self.window.destroy()
        self.ventana_anterior.iniciar_login()

    def button_inventory(self):
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("inventory"),
            relief="flat"
        )
        self.button_2.place(
            x=9.0,
            y=278.9999999999999,
            width=336.0,
            height=72.0
        )

    def open_inventories_view(self):
        self.window.destroy()
        self.inventories.start_inventory()

    def button_create_product(self):
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_create_product,
            relief="flat"
        )
        self.button_3.place(
            x=9.0,
            y=178.9999999999999,
            width=342.0,
            height=75.0
        )

    def open_create_product(self):
        self.window.destroy()
        self.create.start_create_product()

    def button_register_user(self):
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_register,
            relief="flat"
        )
        self.button_4.place(
            x=9.0,
            y=73.99999999999989,
            width=340.0,
            height=80.0
        )

    def open_register(self):
        self.window.destroy()
        self.register.iniciar_register()

    def logo(self):
        self.canvas.create_text(
            70.0,
            15.999999999999886,
            anchor="nw",
            text="ADMINISTRATOR",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            43.744140625,
            34.80435180664051,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            43.937477111816406,
            26.874999999999886,
            image=self.image_image_2
        )

    def start_window(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def start_menu(self):
        self.create_window()
        self.set_up_canvas()
        self.button_sign_off()
        self.button_inventory()
        self.button_create_product()
        self.button_register_user()
        self.logo()
        self.start_window()

