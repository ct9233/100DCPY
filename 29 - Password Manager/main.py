from tkinter import *

WINDOW_COLOR = "#3d4d80"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as file:
        file.write(f"{website_input.get()}  --  {username_input.get()}  --  {password_input.get()}\n")
    website_input.delete(0, END)
    password_input.delete(0, END)

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

website_input = Entry(width=35, bg=WINDOW_COLOR)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
website_input.focus()

username_text = Label(text="Email/Username: ", bg=WINDOW_COLOR)
username_text.grid(row=2, column=0, sticky=E)

username_input = Entry(width=35, bg=WINDOW_COLOR)
username_input.grid(row=2, column=1, columnspan=2, sticky=EW)
username_input.insert(0, "user@email.com")

password_text = Label(text="Password: ", bg=WINDOW_COLOR)
password_text.grid(row=3, column=0, sticky=E)

password_input = Entry(width=21, bg=WINDOW_COLOR)
password_input.grid(row=3, column=1, sticky=EW)

generate_button = Button(text="Generate Password", bg=WINDOW_COLOR)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, bg=WINDOW_COLOR, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()