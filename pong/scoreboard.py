from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,240)

    def rewrite_score(self):
        self.clear()
        self.write(f"{self.score_left}   {self.score_right}" , align = "center", font=("Courier", 35, "normal"))

    def win(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"We have a winner", align="center", font=("Courier", 30, "bold"))