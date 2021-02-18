from tkinter import *


window = Tk()
window.title("Mile to Kilometer Conversion")
window.config(padx=20, pady=20)

input = Entry(width=8)
input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

converted_number = Label(text="0")
converted_number.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

button = Button(text="Convert")
button.grid(column=2, row=3)

window.mainloop()