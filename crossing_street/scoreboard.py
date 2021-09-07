from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270,250)
        self.score = 0

    def update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Level: {self.score}", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", font= ("courier", 32, "bold" ), align = "center")
