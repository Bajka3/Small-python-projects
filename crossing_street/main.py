import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

car_list = []
def generate_cars(number_of_new_cars, level_speed):
    for i in range(number_of_new_cars):
        new_car = CarManager(level_speed)
        car_list.append(new_car)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
scoreboard.update_score()
level_speed = car_manager.STARTING_MOVE_DISTANCE
generate_cars(randint(0,5), level_speed)
gen_const = 0

while game_is_on:
    gen_const += 1
    if gen_const % 4 == 0:
        generate_cars(randint(0,2), level_speed)
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        car.move()

    if player.crossing_finish_line():
        scoreboard.update_score()
        for car in car_list:
            car.speed_up()
        level_speed += car_manager.MOVE_INCREMENT
        gen_const += 1

    for car in car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

