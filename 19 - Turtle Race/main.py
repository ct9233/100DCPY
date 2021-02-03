from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    turtles.append("turtle" + str(i + 1))
    distance = -100
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=(distance + i * 40))

screen.exitonclick()