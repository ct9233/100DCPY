from turtle import Turtle, Screen
import random

# import colorgram

# cg_colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
# for i in cg_colors:
#     rgb_colors.append(i.rgb)
# colors = [tuple(rgb) for rgb in rgb_colors]
# print(colors)

color_list = [(219, 156, 91), (127, 166, 192), (55, 102, 146), (182, 65, 29), (238, 209, 96), (128, 178, 146), (229, 66, 99), (62, 118, 83), (240, 65, 36), (213, 126, 151), (10, 43, 66), (182, 19, 9), (143, 71, 98), (173, 147, 
53), (80, 158, 111), (65, 40, 20), (165, 22, 35), (239, 157, 173), (158, 212, 199), (28, 87, 55), (17, 60, 129), (244, 166, 152), (20, 53, 37), (107, 120, 168), (173, 188, 217), (70, 42, 50)]

turtle = Turtle()
screen = Screen()

screen.colormode(255)

turtle.speed("fastest")



screen.exitonclick()