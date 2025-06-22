# coding exercise
from turtle import Turtle, Screen
tom = Turtle()
screen = Screen()
'f-forward,b-backward,l-left,r-right,c-clear'


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_left():
    new_heading = tom.heading()+20  # adding extra angle to current angle
    tom.setheading(new_heading)  # setting new angle
    tom.forward(10)


def move_right():
    new_heading = tom.heading()-20  # subtracting extra angle to current angle
    tom.setheading(new_heading)  # setting new angle
    tom.forward(10)


def clearscreen():
    tom.clear()  # it clears the screen
    tom.penup()
    tom.home()  # it will take turtle to (0,0)
    tom.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="f")
screen.onkey(fun=move_backward, key="b")
screen.onkey(fun=move_left, key="l")
screen.onkey(fun=move_right, key="r")
screen.onkey(fun=clearscreen, key="c")

screen.exitonclick()
