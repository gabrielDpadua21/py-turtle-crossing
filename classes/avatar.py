from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"

class Avatar(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(START_POSITION)
        self.setheading(90)
        self.color(COLOR)

    def move_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def restart(self) -> None:
        self.goto(START_POSITION)

    def finish_line(self) -> None:
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
