from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X=5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(250,random.randint(-220,220))
        self.speed=5



    def level_up(self):
        global X
        X=X+0.1

    def start(self):
        self.forward(X)




