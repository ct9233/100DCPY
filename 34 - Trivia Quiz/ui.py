from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="black")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Some Question Text", 
            fill="white",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.config(bd=0)
        self.false_button.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.config(bd=0)
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()