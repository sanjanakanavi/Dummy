# prject 11 turtle race
'multiple turtles race '
import random
from turtle import Turtle, Screen

WIDTH, HEIGHT = 400, 400
color_list = ["red", "green", "pink", "orange", "blue",
              "yellow", "black", "brown", "aquamarine", "blanched almond"]


def no_of_turtle():  # gives no of turtles
    count = 0
    while True:
        # taking input no of turtles
        count = int(
            input("how many turtles u want to participate in the race(2-10): "))
        if 2 <= count <= 10:
            return count
        else:
            print("input is not in given range, try again....")


turtles = no_of_turtle()
s1 = Screen()
s1.setup(400, 400)  # setting the screen

x_spacing = WIDTH//(turtles+1)  # diving x axis equally for the no of turtles
turtle_list = []
for i in range(1, turtles+1):  # to iterate turtles
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])  # assigning colors by list
    new_turtle.penup()
    '-WIDTH//2+i*x_spacing will place the turtle acordingly with equal space'
    # -HEIGHT//2+10 is negative part of y axis with a gap of 10 pixel from bottom line
    new_turtle.goto(-WIDTH//2+(i*x_spacing), -HEIGHT//2+10)
    turtle_list.append(new_turtle)


def race():  # to decide speed of the turtles
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randrange(1, 20)
            t.forward(distance)
            x, y = t.pos()
            if y >= HEIGHT//2-40:
                print(f"winner is {t.pencolor()} turtle")
                is_race_on = False


race()
s1.mainloop()
