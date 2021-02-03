from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
racing = False

for i in range(6):
    turtles.append("turtle" + str(i + 1))
    distance = -100
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=(distance + i * 40))

if user_bet:
    racing = True

while racing:
    for turtle in turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()