from turtle import Turtle


class Avatar(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)
        self.color("red")

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
        