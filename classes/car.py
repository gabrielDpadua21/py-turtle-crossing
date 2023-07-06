from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:

    def __init__(self) -> None:
        self.all_cars = []


    def create(self) -> None:
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            random_y = randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)
        
    def move(self) -> None:
        for car in self.all_cars:
            car.backward(START_MOVE_DISTANCE)
        