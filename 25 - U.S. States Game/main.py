import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle_writer = turtle.Turtle()
turtle_writer.penup()
turtle_writer.hideturtle()
states = pandas.read_csv("50_states.csv")
game_continues = True

while game_continues:
    turtle_writer.goto(0, 0)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    for i in states.state:
        if answer_state.title() == i:
            x = int(states[states.state == f"{i}"].x)
            y = int(states[states.state == f"{i}"].y)
            turtle_writer.goto(x, y)
            turtle_writer.write(f"{i}")

screen.exitonclick()