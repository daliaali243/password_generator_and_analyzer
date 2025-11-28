from tkinter import *
from tkinter import messagebox
import random
import string

window = Tk()
window.geometry("400x200")
window.title("Password Generator")
window.config(bg="black")

# Frame لكل العناصر التي يجب أن تختفي عند التحليل أو التوليد
display_frame = Frame(window, bg="black")
display_frame.place(x=0, y=80, width=400, height=120)

entry = Entry(window)
entry.config(fg="black", bg='white')
entry.place(x=10, y=50)

generated_password=''


def copyme():
   global generated_password
   entry.delete(0, END)
   entry.insert(0, generated_password)
   messagebox.showinfo("Password Generator", "Password has been copied ")


def generate(length=12):

        # مسح العناصر القديمة
        for widget in display_frame.winfo_children():
            widget.destroy()


            global generated_password

            # الحد الأدنى المطلوب
            upper_part = random.choices(string.ascii_uppercase, k=2)
            lower_part = random.choices(string.ascii_lowercase, k=2)
            digit_part = random.choices(string.digits, k=2)
            symbol_part = random.choices("!@#$%&*", k=2)

            # بقية الأحرف عشوائية
            remaining = length - 8
            chars = string.ascii_letters + string.digits + "!@#$%&*"
            random_part = random.choices(chars, k=remaining)

            password_list = upper_part + lower_part + digit_part + symbol_part + random_part
            random.shuffle(password_list)

            password = "".join(password_list)


            generated_password = password

        label= Label(display_frame, text=password, fg="white", bg="black")
        label.place(x=200, y=20)

        copy = Button(display_frame, text="Copy Password", fg="black", bg='white', command=copyme)
        copy.place(x=100, y=20)


def analyze():

    # مسح كل النتائج القديمة والازرار
    for widget in display_frame.winfo_children():
        widget.destroy()

    score = 0
    password = entry.get()
    user_password = "".join(password)

    # طول الباسورد
    if len(user_password) >= 12:
        score += 40
    elif len(user_password) > 10:
        score += 22
    elif len(user_password) > 8:
        score += 5
    elif len(user_password) == 8:
        score += 0
    else:
        messagebox.showinfo(message="Password is too short")
        return

    upper = 0
    lower = 0
    digit = 0
    symbol = 0

    for i in user_password:
        if i.isdigit():
            digit+=15
        if i.isupper():
          upper+=15
        if i.islower():
            lower+=15
        if i in "!@#$%^&*()-_=+[]{};:,.<>?/|":
            symbol+=15

    # Uppercase
    if upper >= 2:
        score += 15
    elif upper==1 :
        score += 5

    # Lowercase
    if lower >= 2:
        score += 15
    elif lower==1 :
        score += 5

    # Digits
    if digit >= 2:
        score += 15
    elif digit==1 :
        score += 5

    # Symbols
    if symbol >= 2:
        score += 15
    elif symbol==1 :
        score += 5

    show_score(score)


def show_score(score):

        if score >= 90:
            measure_label = Label(display_frame, text=f"Your password is strong ({score}/100)", fg="green", bg="white")
            measure_label.place(x=10, y=10)

        elif score >= 60:
            measure_label = Label(display_frame, text=f"Your password is good ({score}/100)", fg="green", bg="white")
            measure_label.place(x=10, y=10)

            button = Button(display_frame, text="generate", fg="black", bg="white", command=generate)
            button.place(x=290, y=60)

            generate_lable = Label(display_frame, text='do you want to generate a strong password? ', fg="green", bg="white")
            generate_lable.place(x=0, y=60)

        elif score >= 30:
            measure_label = Label(display_frame, text=f"Your password is medium ({score}/100)", fg="orange", bg="white")
            measure_label.place(x=10, y=10)

            button = Button(display_frame, text="generate", fg="black", bg="white", command=generate)
            button.place(x=290, y=60)

            generate_lable = Label(display_frame, text='do you want to generate a strong password? ', fg="green", bg="white")
            generate_lable.place(x=0, y=60)

        else:
            measure_label = Label(display_frame, text=f"Your password is weak ({score}/100)", fg="red", bg="white")
            measure_label.place(x=10, y=10)

            button = Button(display_frame, text="generate", fg="black", bg="white", command=generate)
            button.place(x=290, y=60)


analyze_button = Button(window, text='analyze', fg="white", bg="gray")
analyze_button.config(command=analyze)
analyze_button.place(x=150, y=45)

label = Label(window, text="enter your password to analyze", fg="white", bg="black")
label.place(x=0, y=10)

window.mainloop()
