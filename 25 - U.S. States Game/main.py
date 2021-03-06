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
score = 0
correct_guesses = []

while game_continues:
    turtle_writer.goto(0, 0)
    answer_state = screen.textinput(title=f"Guess the State - {score}/50 Correct", prompt="                                   What's another state's name?                              ")

    if answer_state.title() == "Exit":
        break

    for i in states.state:
        if answer_state.title() == i:
            x = int(states[states.state == f"{i}"].x)
            y = int(states[states.state == f"{i}"].y)
            turtle_writer.goto(x, y)
            turtle_writer.write(f"{i}")
            if i not in correct_guesses:
                correct_guesses.append(i)
                score += 1

learning_list = [i for i in states.state if i not in correct_guesses]

pandas.DataFrame(learning_list).to_csv("learning_list.csv")

# screen.exitonclick()