from tkinter import *

def button_clicked():
    print("Button clicked")
    my_text = input.get()
    my_label.config(text="Button clicked")

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="Hello World", font=("Arial", 24,"bold"))
#my_label.pack(side="right") # place it into the screen and center, bottom, right, left
#my_label["text"] = "New Text"
my_label.config(text="New Text")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Text")
new_button.grid(column=2, row=0)


# entry
input = Entry(width=10)
#input.pack()
print(input.get())
# cannot mix up grid and pack
input.grid(column=3, row=2)

button_clicked()

window.mainloop()