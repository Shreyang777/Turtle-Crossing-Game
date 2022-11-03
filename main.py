from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car=CarManager()
counter=Scoreboard()

screen.listen()
screen.onkey(tim.move,"Up")

x=0
l=[]

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    x+=1
    counter.counter()
    if x % 4 == 0:
        c1 = CarManager()
        l.append(c1)
    for i in l:
        i.start()
    car.start()

    #Detect Collision
    for i in l:
        if tim.distance(i)<20:
            print("Game over")
            counter.game_over()
            game_is_on=False

    #Detect Finish
    if tim.ycor()>280:
        tim.goto(0,-280)
        for i in l:
            i.level_up()
        counter.level_up()






screen.exitonclick()