from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []

for i in range(3):
    segments.append("segment" + str(i + 1))
    segments[i] = Turtle("square")
    segments[i].color("medium sea green")
    segments[i].penup()
    segments[i].setpos(-i * 20, 0)


screen.exitonclick()