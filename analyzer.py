import hashlib
import requests
from tkinter import *
from tkinter import messagebox
from generate import Generate

class PasswordAnalyzer:
    def __init__(self, display_frame,password_entry):
        self.display_frame = display_frame
        self.generator = Generate(display_frame)
        self.password_entry=password_entry
        self.default_have = ['uppercase letter', 'lowercase letter', 'numbers', 'symbol']
        self.have = []
        self.score = 0

    def paste_password(self):

            copied = self.display_frame.clipboard_get()
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, copied)

    def user_common_password(self):
        return [
            '123456','1234567','012345678','0123456789',
            '1234567890','12345','password','abc123',
            'welcome','admin'
        ]

    def check_api(self, password):
        sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]

        try:
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            res = requests.get(url)

            if res.status_code != 200:
                return "API error"

            for line in res.text.splitlines():
                h, count = line.split(":")
                if h == suffix:
                    return f"Password appeared in {count} breaches"
            return "password not found in any known breach"

        except:
            return "API error"

    def analyze_strength(self, password):

        for widget in self.display_frame.winfo_children():
            widget.destroy()

        if password == "":
            messagebox.showinfo("Error", "Please enter a password")
            return

        self.score = 0
        self.have = []

        length = len(password)
        if length >= 12:
            self.score += 40
        elif length >= 7:
            self.score += 20
        else:
            self.score += 5

        upper = lower = digit = symbol = 0
        for c in password:
            if c.isupper(): upper += 1
            if c.islower(): lower += 1
            if c.isdigit(): digit += 1
            if c in "!@#$%^&*()-_=+[]{};:,.<>?/|": symbol += 1

        if upper > 1:
            self.score += 15
            self.have.append("uppercase letter")
        if lower > 1:
            self.score += 15
            self.have.append("lowercase letter")
        if digit >1:
            self.score += 15
            self.have.append("numbers")
        if symbol > 1:
            self.score += 15
            self.have.append("symbol")

        self.show_score(password)

    def recommendation(self):
       missing =[]
       for i in self.default_have:
            if i not in self.have:
               missing.append(i)
       if len(missing) ==0:
               return "Password has all requirements"
       return "You should add more: " + ", ".join(missing)

    def generate_password(self):

        strong= self.generator.generate_passwored()



    def show_score(self, password):
        if self.score >= 90:
            strength ='strong'
            color = 'green'
        elif self.score >= 50:
            strength ='medium'
            color = 'orange'
        else:
            strength ='week'
            color = 'red'
        result = self.check_api(password)

        Label(
            self.display_frame,
            text=f"Password strength score: {self.score}/100\n\n    {result}",
            fg="black",
            bg="white",
            font=("Arial", 12)
        ).pack(pady=5)
        Label(
            self.display_frame,
            text=f'your password strength is {strength}',
            fg=color,
            bg='white'
        ).pack(pady=5)

        if self.score<90:
         Label(
            self.display_frame,
            text=self.recommendation(),
            fg="black",
            bg="white",
            wraplength=350
        ).pack(pady=5)

        if self.score < 90:
            Label(
                self.display_frame,
                text="Do you want to generate a strong password?",
                fg="black",
                bg="white"
            ).pack(pady=5)

            Button(
                self.display_frame,
                text="Generate",
                command=self.generate_password
            ).pack(pady=5)