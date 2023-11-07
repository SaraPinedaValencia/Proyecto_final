import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class RegisterSale:

    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior

        self.window = None
        self.canvas = None

        self.button_image_1 = None
        self.button_1 = None

        self.entry_image_1 = None
        self.entry_image_2 = None

        self.image_image_1 = None
        self.image_image_2 = None
        self.image_image_3 = None

        self.quantity_data = None
        self.code_data = None

        self.code_current = None
        self.quantity_current = None

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
            800.0,
            fill="#FFFFFF",
            outline="")

    def button_register_sale(self):
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_information,
            relief="flat"
        )
        self.button_1.place(
            x=25.0,
            y=361.0,
            width=312.0,
            height=78.0
        )

    def quantity_register_sale(self):
        self.canvas.create_text(
            146.0,
            309.0,
            anchor="nw",
            text="QUANTITY",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            46.0,
            302.0,
            313.0,
            303.0,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            193.0,
            287.0,
            image=self.entry_image_1
        )
        self.quantity_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.quantity_data.place(
            x=73.0,
            y=275.0,
            width=240.0,
            height=22.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            59.0,
            289.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            58.0,
            278.0,
            image=self.image_image_2
        )

    def code_register_sale(self):
        self.canvas.create_text(
            162.0,
            223.0,
            anchor="nw",
            text="CODE",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            46.0,
            218.0,
            313.0,
            219.0,
            fill="#000000",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            193.0,
            203.0,
            image=self.entry_image_2
        )
        self.code_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.code_data.place(
            x=73.0,
            y=191.0,
            width=240.0,
            height=22.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            58.0,
            203.0,
            image=self.image_image_3
        )

    def logo(self):
        self.canvas.create_text(
            79.0,
            93.0,
            anchor="nw",
            text="REGISTER SALE",
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

    def get_information_quantity(self):
        if self.quantity_data.get():
            self.quantity_current = self.quantity_data.get()
        else:
            messagebox.showerror("Error", "El campo del quantity está vacío")

    def get_information(self):
        self.get_information_code()
        self.get_information_quantity()

        print(self.code_current, self.quantity_current)

    def start_register_sale(self):
        self.create_window()
        self.create_canvas()
        self.button_register_sale()
        self.quantity_register_sale()
        self.code_register_sale()
        self.logo()
        self.start_window()


'''ventana = RegisterSale()
ventana.start_register_sale()'''
