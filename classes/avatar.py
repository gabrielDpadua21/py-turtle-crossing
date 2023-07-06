from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"

class Avatar(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(START_POSITION)
        self.setheading(90)
        self.color(COLOR)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        