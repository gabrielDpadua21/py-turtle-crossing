from turtle import Screen
from time import sleep
from classes.avatar import Avatar
from classes.car import Car


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Game")
    screen.tracer(0)
    screen.listen()
    GAME_ON = True

    avatar = Avatar()
    cars = Car()

    screen.onkey(avatar.move_up, "Up")

    while GAME_ON:
        sleep(0.1)
        screen.update()
        cars.create()
        cars.move()
        
        for car in cars.all_cars:
            if car.distance(avatar) < 20:
                GAME_ON = False


    screen.exitonclick()
    