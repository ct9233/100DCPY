from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow green")
        self.setheading(90)
        self.penup()
        self.set_start()

    def set_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        else:
            self.set_start()
