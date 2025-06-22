# coding exercise on turtle
from turtle import Turtle
import random
tom = Turtle()
colors = ["red", "green", "pink", "orange", "blue", "gray", "alice blue", "aquamarine",
          "brown", "burlywood", "chocolate1", "cyan", "beige", "black", "blanched almond"]
for i in range(3, 9):
    angle = 360/i
    tom.pencolor(random.choice(colors))
    for _ in range(i):
        tom.forward(100)
        tom.rt(angle)
tom.screen.mainloop()
