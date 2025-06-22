# turtle graphics
'''from turtle import Turtle/from turtle import */import turtle as t: we can import like this'''
from turtle import Turtle, Screen
s1 = Screen()  # creating an object for screen class
tom = Turtle()  # creating an object for class turtle
tom.shape("turtle")
tom.pencolor("red")  # to change the ink color
tom.fillcolor("green")  # to fill the color ,indicated in turtle also
'or we can use color("pencolor","fillcolor")method also'
tom.color("purple", "pink")
'begin_fill() and end_fill() methos used to fill the color'
tom.begin_fill()
tom.circle(100)  # drawing a circle
tom.end_fill()
tom.rt(90)  # turning turtle right side
'penup() and pendown() methods are like lifting a pen up and down'
tom.penup()
print(tom.isdown())  # return true or false whether pen is up or down
tom.forward(100)
tom.pendown()
tom.pensize(5)  # increasing thickness of the ink
tom.hideturtle()  # making turtle invisible
print(tom.isvisible())  # it will check if turtle is visible or no
tom.begin_fill()
tom.circle(50)
tom.end_fill()
'goto(x,y) method finds the position,x can be in single or pair,y can be single or none'
'goto,pos(),position() are all same or similar'
print(tom.pos())  # finidng the turtle position
tom.goto(-100, -100)  # putting turtle into specific position
tom.showturtle()  # it is going to show the turtle
# tom.forward(100)
s1.mainloop()  # s1 is an object here for screen class to operate with screen
