from abc import ABC, abstractmethod  # importing astractmethods from abc module


class Vehicle(ABC):  # way to make a class as abstract class
    def __init__(self, n):
        self.no_of_tires = n

    @abstractmethod  # way to make a method as abstract method
    def start(self):
        pass

    def display(self):  # can create normal methods also in abstract class
        print("hi im calling from vehicle class")
