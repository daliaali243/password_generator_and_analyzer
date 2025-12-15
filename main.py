from tkinter import *
from analyzer import PasswordAnalyzer


window = Tk()
window.geometry("400x300")
window.configure(bg="white")
window.title("Password Analyzer")


display_frame = Frame(window, bg="white")

display_frame.place(x=0, y=80)
entry = Entry(window, width=30,bg="#EAEAEA")
entry.place(x=50, y=20)

analyzer = PasswordAnalyzer(display_frame, entry)




def analyze():
 password = entry.get()
 analyzer.analyze_strength(password)

analyze_button = Button(window, text="Analyze Password",bg='#C1CDCD' ,command=analyze)
analyze_button.place(x=50, y=50)
Button(
        window,
        text="Paste",
        command=analyzer.paste_password,
        bg='#C1CDCD'
    ).place(x=200, y=50)

window.mainloop()
