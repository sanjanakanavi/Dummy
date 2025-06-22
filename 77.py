# diamond problem technique
"""                        parent
                _____________|______________
                |                           |                  
            child 1                        child 2
                |___________ _______________|
                            |                                  |
                         child 3                            
in this condition child 3 will be confused to fetch data if same methods are present in all other 3 classes
so by using mro method we can overcome it i.e mro method will use C3 linearization algorithm to solve diamond problem"""


class A:  # parent
    def display(self):
        print("display from A class")


class B(A):  # child 1
    def display(self):
        print("display from B class")


class C(A):  # child 2
    def display(self):
        print("display from C class")


class D(B, C):  # child 3 = child 1, child 2
    def display(self):
        print("display from D class")


d1 = D()
'first it will search in its own class then first parent then second parent then parents parent class ,this is how mro follows in diamond prbm'
d1.display()
print(D.mro())
