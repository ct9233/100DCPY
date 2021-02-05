from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("blue violet")
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("crimson")
        self.write("GAME OVER", align="center", font=("Verdana", 16, "normal"))


