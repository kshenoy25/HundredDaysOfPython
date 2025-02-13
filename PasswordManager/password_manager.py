from tkinter import *

from PasswordManager.main import logo_img

# UI Setup

window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo1_img = PhotoImage(file="logo.png")
canvas.create_image(image=logo_img)



window.mainloop()