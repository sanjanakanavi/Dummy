from turtle import Turtle, Screen
import turtle
import random
tom = Turtle()
s1 = Screen()
turtle.colormode(255)
tom.speed(0)
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.pencolor((r, g, b))
    tom.circle(100)
    tom.left(5)
    if tom.heading() == 0:
        break
s1.exitonclick()
