import tkinter as tk
from tkinter import ttk

from Controller import Login


class LoginView(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.controller = controller
        self.place(x=0, y=0, width=600, height=400)

        tempx = 180
        tempy = 130

        self.remember_me = tk.BooleanVar()
        self.remember_me.set(True)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.login_status = tk.BooleanVar()

        name_label = ttk.Label(self, text="Name: ")
        name_label.place(x=tempx + 10, y=tempy)

        name_entry = ttk.Entry(self, textvariable=self.username)
        name_entry.place(x=tempx + 60, y=tempy)

        password_label = ttk.Label(self, text="Password: ")
        password_label.place(x=tempx - 8, y=tempy + 20 + 5)

        password_entry = ttk.Entry(self, textvariable=self.password, show='*')
        password_entry.place(x=tempx + 60, y=tempy + 20 + 5)

        checkbox = tk.Checkbutton(self, text="Remember Me", variable=self.remember_me)
        checkbox.place(x=tempx + 65, y=tempy + 55)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.place(x=tempx + 83, y=tempy + 80)

        self.login_status.set(False)

    def set_login_status_true(self):
        self.login_status.set(True)

    def get_login_status(self):
        return self.login_status.get()

    def login(self):
        if self.username.get() and self.password.get():
            self.login_button["state"] = tk.DISABLED
            Login.login(self.username.get(), self.password.get(),
                        self.remember_me.get(), self)


class LoginWaitingView(tk.Frame):
    pass
