# coding exercise on turtle
from turtle import Turtle, Screen
import random
import turtle
tom = Turtle()
s1 = Screen()
turtle.colormode(255)
print(s1.screensize())  # by this u can check screen size
s1.screensize(500, 500)
tom.penup()
tom.speed(10)
tom.hideturtle()
for i in range(400):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.pencolor((r, g, b))
    tom.dot(20)  # draws dot of size 20
    tom.goto(random.randint(-300, 300), random.randint(-300, 300))

s1.exitonclick()
