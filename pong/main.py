from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
from random import randrange

screen = Screen()
paddle = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
WIN = 5

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game by Bajka")
screen.tracer(0)

line = Turtle()
line.pensize(4)
line.color("white")
line.penup()
line.goto(0, -285)
line.pendown()
line.left(90)

def draw_line():
    for i in range(30):
        line.forward(20)
        line.penup()
        line.forward(20)
        line.pendown()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down, "s")

game_is_on = True
scoreboard.rewrite_score()
while game_is_on:
    draw_line()
    screen.update()
    a = (ball.xcor() > 330 and (ball.heading() <70 or ball.heading()>-70) and ball.distance(paddle) < 55)
    b = (ball.distance(paddle2) < 55 and ball.xcor() <= -330)
    if a or b:
        ball.paddle_bounce()
    elif ball.xcor() > 400:
        scoreboard.score_left += 1
        ball.__init__()
        ball.setheading(randrange(-60, 60)+180)
    elif ball.xcor() < -410:
        scoreboard.score_right += 1
        ball.__init__()
        ball.setheading(randrange(-60, 60))
    scoreboard.rewrite_score()
    if ball.xcor() < 450 and ball.xcor() > -450:
        ball.move()
    if scoreboard.score_left == WIN or scoreboard.score_right == WIN:
        game_is_on = False
        scoreboard.win()
    time.sleep(0.01)

screen.exitonclick()

