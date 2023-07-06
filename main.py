from turtle import Screen
from time import sleep
from classes.avatar import Avatar


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Game")
    screen.listen()
    GAME_ON = True

    avatar = Avatar()

    screen.onkey(avatar.move_up, "Up")

    while GAME_ON:
        sleep(0.1)
        screen.update()


    screen.exitonclick()
    