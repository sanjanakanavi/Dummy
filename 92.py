# turtle in python
import turtle
turtle.getscreen()  # this will get a screen only for second,this method is optional
'turtle.screen() will also show screen'
'many ways are there to hold a screen '

'''we can control the speed of turtle by speed() method ,by parameter 0 to 10
  0:fastest,1:slowest,3:slow,6:normal,10:fast this way'''
turtle.speed(1)

turtle.forward(100)  # this will move a turtle forwad here 100 pixel
turtle.bk(100)  # this will move backward
# here wee can give shapes only :arror,turtle,circle,square,triangle,classic
turtle.shape("turtle")
print(turtle.shape())  # ths will print a shape of turtle in terminal
turtle.left(90)  # turtle turns left with an angle how much u enter
turtle.forward(100)
turtle.rt(45)  # turtle turns right with an angle how much u enter
turtle.forward(100)
turtle.lt(60)  # lt also for left turn
turtle.circle(100)  # enter radius as parameter
# after execution also it will hold the screen,wont close when u click on it
turtle.mainloop()
'when we want more turtles then we use oops concept ,we create obj for every turtle'
t = turtle.Turtle()  # this is creating an object on Turtle class
''' this will hold a screen untill you click on that screen,used as lastmethod
turtle.exitonclick()'''
turtle.done()  # same as exitonclick its a terminator
