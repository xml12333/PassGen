from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for c in range(randint(8, 10))]
    password_list += [choice(symbols) for c in range(randint(2, 4))]
    password_list += [choice(numbers) for c in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(c for c in password_list)

    password_input.delete(0, END)
    password_input.insert(END, string=f"{password}")
    pyperclip.copy(password)


def add_pass():
    website = website_input.get()
    password = password_input.get()
    email = email_user_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "":
        messagebox.showwarning(title="Website",
                               message=f"Website is Empty")
        return
    if password == "":
        messagebox.showwarning(title="Password",
                               message=f"Password is Empty")
        return
    if email == "":
        messagebox.showwarning(title="Email\ User",
                               message="Email\ User is Empty")
        return
    try:
        with open("data/data.json", "r") as f:
            d = json.load(f)
    except FileNotFoundError:
        with open("data/data.json", "w") as f:
            json.dump(new_data, f, indent=4)
    else:
        d.update(new_data)
        with open("data/data.json", "w") as f:
            json.dump(d, f, indent=4)
    finally:
        website_input.delete(0, END)
        email_user_input.delete(0, END)
        email_user_input.insert(END, "admin@a.ru")
        password_input.delete(0, END)


def search_pass():
    website =  website_input.get()
    try:
        with open("data/data.json", "r") as f:
            d = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title=f"{website}",
                               message=f"No data file found")
    else:
        if website in d:
            messagebox.showwarning(title=f"{website}",
                           message=f"{d[website]['email']}\n{d[website]['password']}")
        else:
            messagebox.showwarning(title=f"{website}",
                                   message=f"No details found")


window = Tk()
window.title("Passowrd Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
website_lbl = Label(text="Website:", bg="white").grid(column=0, row=1)
website_input = Entry(width=31, justify=LEFT)
website_input.grid(sticky=W, column=1, row=1)
website_input.focus()
search_btn = Button(text="Search", width=14, command=search_pass, justify=RIGHT).grid(sticky=E, column=1, row=1,
                                                                                      columnspan=2)
email_user_lbl = Label(text="Email/Username:", bg="white").grid(column=0, row=2)
email_user_input = Entry(width=54, justify=LEFT)
email_user_input.grid(sticky=W, column=1, row=2, columnspan=2)
email_user_input.insert(END, "admin@a.ru")
password_lbl = Label(text="Password:", bg="white").grid(column=0, row=3)
password_input = Entry(width=31, justify=LEFT)
password_input.grid(sticky=W, column=1, row=3)
generate_btn = Button(text="Generate Password", command=generate_pass, justify=RIGHT).grid(sticky=E, column=1, row=3,
                                                                                           columnspan=2)
add_btn = Button(text="Add", command=add_pass, width=46, justify=LEFT).grid(sticky=W, column=1, row=4,
                                                                            columnspan=2)
window.mainloop()
