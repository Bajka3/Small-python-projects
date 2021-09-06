from turtle import Turtle
from random import randint

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(60)
        self.ball_speed = 5

    def move(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            head = 360 - self.heading()
            self.setheading(head)
        self.forward(self.ball_speed)


    def paddle_bounce(self):
        head = 180 - self.heading()
        self.ball_speed +=2
        self.setheading(head)





