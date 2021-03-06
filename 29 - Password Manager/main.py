from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WINDOW_COLOR = "#3d4d80"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Cannot proceed", message="Please make sure no fields have been left empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# -------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Alert", message="No details for the website exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="Information", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WINDOW_COLOR)

canvas = Canvas(width=200, height=200, bg=WINDOW_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website: ", bg=WINDOW_COLOR)
website_text.grid(row=1, column=0, sticky=E)

website_input = Entry(width=21, bg=WINDOW_COLOR)
website_input.grid(row=1, column=1, sticky=EW)
website_input.focus()

search_button = Button(text="Search", bg=WINDOW_COLOR, command=find_password)
search_button.grid(row=1, column=2, sticky=EW, padx=(3, 0))

username_text = Label(text="Email/Username: ", bg=WINDOW_COLOR)
username_text.grid(row=2, column=0, sticky=E)

username_input = Entry(width=35, bg=WINDOW_COLOR)
username_input.grid(row=2, column=1, columnspan=2, sticky=EW, pady=2)
username_input.insert(0, "user@email.com")

password_text = Label(text="Password: ", bg=WINDOW_COLOR)
password_text.grid(row=3, column=0, sticky=E)

password_input = Entry(width=21, bg=WINDOW_COLOR)
password_input.grid(row=3, column=1, sticky=EW)

generate_button = Button(text="Generate Password", bg=WINDOW_COLOR, command=generate_password)
generate_button.grid(row=3, column=2, padx=(3, 0))

add_button = Button(text="Add", width=36, bg=WINDOW_COLOR, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, pady=3)

window.mainloop()