import random
import string
from tkinter import Label, Button, Frame, messagebox


class Generate:
    def __init__(self, display_frame):
        self.display_frame = display_frame
        self.generated_password = ""
        self.password_label = None
        self.copy_btn = None
        self.save_btn = None

    def generate_passwored(self):
        length = 12


        for widget in self.display_frame.winfo_children():
            widget.destroy()


        upper_part = random.choices(string.ascii_uppercase, k=2)
        lower_part = random.choices(string.ascii_lowercase, k=2)
        digit_part = random.choices(string.digits, k=2)
        symbol_part = random.choices("!@#$%&*", k=2)

        remaining = length - 8
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        random_part = random.choices(chars, k=remaining)

        password_list = upper_part + lower_part + digit_part + symbol_part + random_part
        random.shuffle(password_list)
        self.generated_password = "".join(password_list)


        self.password_label = Label(
            self.display_frame,
            text=self.generated_password,
            fg="black",
            bg="white",
            font=("Arial", 12, "bold")
        )
        self.password_label.pack(pady=10)


        btn_frame = Frame(self.display_frame, bg="white")
        btn_frame.pack()


        self.copy_btn = Button(btn_frame, text="Copy", command=self.copy_password, width=10,bg='#C1CDCD')
        self.copy_btn.pack(side="left", padx=5)


        self.save_btn = Button(btn_frame, text="Save", command=self.save_password, width=10,bg='#C1CDCD')
        self.save_btn.pack(side="left", padx=5)

        return self.generated_password

    def copy_password(self):
        self.display_frame.clipboard_clear()
        self.display_frame.clipboard_append(self.generated_password)

    def save_password(self):
        try:
            with open("passwords.txt", "a") as f:
                f.write(self.generated_password + "\n")
        except FileNotFoundError:
            messagebox.showerror()
