from turtle import Turtle
import random

COLORS = ["crimson", "orange", "yellow", "cyan", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_y = random.randrange(-240, 250)
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2)
        new_car.penup()
        new_car.goto(320, random_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in range(len(self.cars)):
            new_x = self.cars[car].xcor() - self.car_speed
            self.cars[car].goto(new_x, self.cars[car].ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
