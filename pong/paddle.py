from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position,0)
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        if self.ycor()<240:
            self.setheading(90)
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)







