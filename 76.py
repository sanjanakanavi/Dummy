# hybrid inheritance in python
"""example for hybrid inheritance,mix of 2 or more type of inheritance
parent 1 
      |
   child 1     parent 2
      |______   ____|
              |
            child 2"""


class A:
    def display(self):
        print("display from A class")


class B(A):
    def display(self):
        print("display from B class")


class C:
    def show(self):
        print("hi from C class")


class D(B, C):
    def display(self):
        print("display from D class")


d1 = D()
print(D.mro())
