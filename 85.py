# duck typing in polymorphism
'first we will see static and dynamic typing'

'''here in square method x accepts both integer and float value,so x is acting dynamically
we dont have to mention int or float'''


def square(x):
    return x*x


print(square(5))
print(square(4.5))
'''in duck typing class doesnot matter ,what matters is if any method we call from class is defined to object or no,
if object can access its defined method then we can access it outside the class also'''
'example :taking 3 class with its own methods'


class Duck:
    def swim(self):
        print("im duck and i can swim")

    def speaks(self):
        print("quack quack")


class Dog:
    def swim(self):
        print("im dog and i can swim")

    def speaks(self):
        print("woof wooof")


class Person:
    def speaks(self):
        print("blah blah blah")


'creating a method with a parameters which accepts objects'


def display(object_duck, object_dog, object_person):  # zparameters accepting objects
    print("methods of duck class")
    object_duck.swim()  # accessing method of duck class
    object_duck.speaks()
    print("methods of dog class")
    object_dog.swim()
    object_dog.speaks()
    print("methods of person class")
    object_person.speaks()  # accessing method of person class


'creating objects for all classes'
duck = Duck()
dog = Dog()
p = Person()
display(duck, dog, p)  # calling function and passing object as parameter

