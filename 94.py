# coding exercise on turtle
from turtle import Turtle, Screen
tom = Turtle()
s1 = Screen()
'logic for dotted line'
for i in range(15):  # 10 times loop
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
s1.mainloop()
