# coding exercise
from turtle import Turtle, Screen
tom = Turtle()
s1 = Screen()
tom.color("red", "yellow")
tom.width(3)
tom.begin_fill()
tom.speed(10)
while True:
    tom.forward(400)
    tom.left(170)
    if tom.heading() == 0:  # heading() gives starting point of turtle
        break  # loop stops when it returns to starting position
tom.end_fill()
s1.mainloop()
