from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#b1ddc6"
data = pandas.read_csv("data/french_words.csv")
word_list = data.to_dict(orient="records")

def new_word():
    random_word = random.choice(word_list)
    canvas.itemconfig(card_front_title, text="French")
    canvas.itemconfig(card_front_word, text=random_word["French"])

# ----------------------------- UI Setup -----------------------------  #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_front_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_front_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.config(bd=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_word)
right_button.config(bd=0)
right_button.grid(row=1, column=1)

new_word()

window.mainloop()