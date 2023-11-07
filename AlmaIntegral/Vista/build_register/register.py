import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
from AlmaIntegral.Modelo.Users import UserManagement

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Register:

    def __init__(self, ventana_anterior2):
        self.ventana_anterior2 = ventana_anterior2
        self.user_management = UserManagement("../assets/Inventory.db")

        self.window = None
        self.canvas = None

        self.button_image_1 = None
        self.button_image_2 = None

        self.image_image_1 = None
        self.image_image_2 = None
        self.image_image_3 = None
        self.image_image_4 = None

        self.entry_image_4 = None
        self.entry_image_3 = None
        self.entry_image_2 = None
        self.entry_image_1 = None

        self.entry_4 = None
        self.entry_3 = None
        self.entry_2 = None
        self.entry_1 = None

        self.name_data = None
        self.email_data = None
        self.password_data = None
        self.confirm_password_data = None

        self.name_actual = None
        self.email_actual = None
        self.password_actual = None
        self.confirm_password_actual = None

    def crear_ventana(self):
        self.window = Tk()
        self.window.geometry("360x800")
        self.window.configure(bg="#58A76E")

    def crear_canvas(self):
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

    def button_back(self):
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
            x=110.0,
            y=617.0,
            width=138.0,
            height=62.0
        )

    def back_to_menu(self):
        self.window.destroy()
        self.ventana_anterior2.start_menu()

    def button_register(self):
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.obtener_data,
            relief="flat"
        )
        button_2.place(
            x=23.0,
            y=512.0,
            width=312.0,
            height=91.0
        )

    def password(self):
        self.canvas.create_rectangle(
            46.0,
            375.0,
            313.0,
            376.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            141.0,
            376.0,
            anchor="nw",
            text="PASSWORD",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            193.0,
            435.5,
            image=self.entry_image_1
        )
        self.confirm_password_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.confirm_password_data.place(
            x=73.0,
            y=425.0,
            width=240.0,
            height=19.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            59.0,
            435.0,
            image=self.image_image_1
        )

    def confirm_password(self):
        self.canvas.create_rectangle(
            46.0,
            449.0,
            313.0,
            450.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            111.0,
            454.0,
            anchor="nw",
            text="CONFIRMPASSWORD",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            193.0,
            361.0,
            image=self.entry_image_2
        )
        self.password_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.password_data.place(
            x=73.0,
            y=350.0,
            width=240.0,
            height=20.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            59.0,
            360.0,
            image=self.image_image_2
        )

    def email_id(self):
        self.canvas.create_text(
            141.0,
            297.0,
            anchor="nw",
            text="EMAIL ID",
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

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            193.0,
            286.0,
            image=self.entry_image_3
        )
        self.email_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email_data.place(
            x=73.0,
            y=278.0,
            width=240.0,
            height=14.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            59.0,
            286.0,
            image=self.image_image_3
        )

    def full_name(self):
        self.canvas.create_text(
            141.0,
            230.0,
            anchor="nw",
            text="FULL NAME",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_rectangle(
            46.0,
            229.0,
            313.0,
            230.0,
            fill="#000000",
            outline="")

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            193.0,
            214.0,
            image=self.entry_image_4
        )
        self.name_data = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.name_data.place(
            x=73.0,
            y=202.0,
            width=240.0,
            height=22.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            59.0,
            218.0,
            image=self.image_image_4
        )

    def logo(self):
        self.canvas.create_text(
            119.0,
            126.0,
            anchor="nw",
            text="REGISTER",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

    def iniciar_ventana(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def obtener_datos_name(self):
        if self.name_data.get():
            self.name_actual = self.name_data.get()
            # mandar a base de datos
        else:
            messagebox.showerror("Error", "El campo del nombre está vacío")

    def obtener_datos_email(self):
        if self.email_data.get():
            self.email_actual = self.email_data.get()
        else:
            messagebox.showerror("Error", "El campo de correo electrónico está vacío")

    def obtener_datos_password(self):
        if self.password_data.get():
            self.password_actual = self.password_data.get()
        else:
            messagebox.showerror("Error", "El campo de contraseña está vacío")

    def obtener_datos_confirm_password(self):
        if self.confirm_password_data.get():
            self.confirm_password_actual = self.confirm_password_data.get()
        else:
            messagebox.showerror("Error", "El campo de confirmar contraseña está vacío")

    def obtener_data(self):
        self.obtener_datos_name()
        self.obtener_datos_email()
        self.obtener_datos_password()
        self.obtener_datos_confirm_password()
        if not self.user_management.verify_user_exist(self.email_actual):
            if self.user_management.verify_email(self.email_actual):
                if self.password_actual == self.confirm_password_actual:
                    self.user_management.save_register(self.name_actual, self.email_actual, self.password_actual, "Administrador")
                else:
                    messagebox.showerror("Error", "El campo de contrseña es inválido")
            else:
                messagebox.showerror("Error", "El campo de email es inválido")
        else:
            messagebox.showerror("Error", "El email ya se encuentra registrado")

        print(self.name_actual, self.email_actual, self.password_actual, self.confirm_password_actual)

    def iniciar_register(self):
        self.crear_ventana()
        self.crear_canvas()
        self.button_back()
        self.button_register()
        self.confirm_password()
        self.password()
        self.email_id()
        self.full_name()
        self.logo()
        self.iniciar_ventana()

'''cosa = Register()
cosa.iniciar_register()'''

