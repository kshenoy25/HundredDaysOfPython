from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Forge")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic", "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, width=98, height=97)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, width=98, height=98)
right_button.grid(row=1, column=1)

window.mainloop()