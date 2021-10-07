from turtle import Turtle, Screen

john = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch!")


def move_forwards():
    john.forward(20)


def move_backwards():
    john.backward(20)


def move_left():
    john.left(20)


def move_right():
    john.right(20)


def clear():
    john.clear()
    john.penup()
    john.home()
    john.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
