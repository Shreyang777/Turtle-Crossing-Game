from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240,270)
        self.score=1



    def counter(self):
        self.pendown()
        self.pencolor("black")
        self.write(f"Level: {self.score}",align="center",font = ("Courier", 18, "normal"))

    def level_up(self):
        self.clear()
        self.goto(-240,270)
        self.score=self.score+1
        self.write(f"Level: {self.score}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0)

        self.write(f"GAME OVER", align="center", font=("Courier", 18, "normal"))
