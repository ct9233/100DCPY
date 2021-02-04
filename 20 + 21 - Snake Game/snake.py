from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.segments.append("segment" + str(i + 1))
            self.segments[i] = Turtle("square")
            self.segments[i].color("medium sea green")
            self.segments[i].penup()
            self.segments[i].setpos(-i * 20, 0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)