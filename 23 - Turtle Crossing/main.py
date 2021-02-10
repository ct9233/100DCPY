import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
car_ticker = 0
while game_is_on:
    car_ticker += 1
    time.sleep(0.1)
    screen.update()
    if car_ticker % 6 == 0:
        car_ticker = 0
        car_manager.create_car()
    car_manager.move_cars()
    

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.ycor() > 280:
        player.set_start()
        car_manager.level_up()
        scoreboard.increase_level()

scoreboard.game_over()


screen.exitonclick()