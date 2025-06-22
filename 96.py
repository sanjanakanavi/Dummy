# coding exercise on turtle
import turtle
from turtle import Turtle
import random
turtle.colormode(255)  # setting colormode first as 255 for turtle module
tom = Turtle()
tom.pensize(5)
tom.shape("turtle")
for i in range(100):
    r = random.randint(0, 255)  # randomly choosing value of rgb
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    'setheading will turn turtle to that angle automatically'
    # 0 to 360,360 is excluded,skips 90 steps
    tom.setheading(random.randrange(0, 360, 90))
    tom.pencolor((r, g, b))  # setting color for pen,mix of rgb randomly
    tom.forward(30)
tom.screen.mainloop()
