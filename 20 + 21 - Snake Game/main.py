from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []

for i in range(3):
    segments.append("segment" + str(i + 1))
    segments[i] = Turtle("square")
    segments[i].color("medium sea green")
    segments[i].penup()
    segments[i].setpos(-i * 20, 0)

game_on = True

while game_on:
    screen.update()

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()