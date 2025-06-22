# abstraction in python
from abstract81 import Vehicle
'abstraction is a process to hide implimentation details from the user and showing only essential details to the user'
'with the help of abc(abstract base classes) module in python we can make our classes and methods abstract'
'every abstract class should have atleast one abstract method or can be more'
'we cannot create object for an abstract class'
'everyclass which inherit from abstract class should have its parents abstract method'
'abstract method is method which only deeclaration not implimentation'


class Bike(Vehicle):  # inheriting abstract into normal class
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):  # must define abstract method
        print("start with kick")


class Scooty(Vehicle):
    def __init__(self, n):
        self.no_of_tires = n

    def start(self):
        print("self start")


class Car(Vehicle):
    def __init__(self, n, x):
        self.no_of_tires = n
        self.no_of_gears = 6

    def start(self):
        print("start with key")
