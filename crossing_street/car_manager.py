from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,level_speed):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.setheading(180)
        self.goto(310, randrange(-240, 265, 25))
        self.color(choice(COLORS))
        self.speed = level_speed

    def move(self):
        self.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT









