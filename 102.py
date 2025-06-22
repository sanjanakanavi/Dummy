# python event listeners
'these will perform actions like click,clicking keys ,etc using turtle module'
from turtle import Turtle, Screen
screen = Screen()
tom = Turtle()


def up():  # to create actions
    tom.setheading(90)  # or tom.left(90)
    tom.forward(20)


def down():  # to create actions
    tom.setheading(270)  # or tom.right(90)
    tom.forward(20)


def left():  # to create actions
    tom.setheading(180)  # or tom.left(180)
    tom.forward(20)


def right():  # to create actions
    tom.setheading(0)  # or tom.right(0)
    tom.forward(20)


def clearscreen():
    tom.clear()  # it clears the screen
    tom.penup()
    tom.home()  # it will take turtle to (0,0)
    tom.pendown()


screen.listen()  # it will capture actions happen on screen
screen.onkey(fun=up, key="Up")  # should pass function and keyname
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=clearscreen, key="c")
screen.exitonclick()
