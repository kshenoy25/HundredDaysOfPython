from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# --------- Generate Password --------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #nr_letters = random.randint(8,10)
    #nr_symbols = random.randint(2,4)
    #nr_numbers = random.randint(2,4)

    # list comprehensions
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    print(f"Your password is: {password}")

    # generating a new password and displayed in the GUI password section
    password_entry.insert(0, password)
    pyperclip.copy(password)

# --------- Save Password --------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="PLease fill all fields.")
    # message box
    else:
        #is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
        #                                              f"\nPassword: {password} \nIs it okay to save?")
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            # updating old data with new data
            data.update(new_data)


            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            #data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# --------- UI Setup --------- #

window = Tk()
window.title("Password Manager")

# add padding
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo1_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo1_img)
canvas.grid(row=0, column=1)
#canvas.pack()

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Password:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kunal25@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()