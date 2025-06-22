# operator overloading: it is the use of operators dynamically
print(1+2)  # here + operator adds
print("1"+"2")  # here + operator concatinate

'every time u use + ,behind the scene __add__ method is called'
'these are special methods we can also use'
print(int.__add__(1, 2))  # this adds numbers
print(str.__add__("1", "2"))  # this time it concatinates
'like this we can use more special methods'

'example for operating overloading'


class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):  # inbuilt function,making it perform addition of complexnumbers(overloading)
        return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
    '                  c1         c2            c1              c2'


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 3)
'when u use + operator btw objects ,it calls __add__ method ,it consider self as c1 and other as c2'
print(c1+c2)  # adding 2 complex numbers


'another example for operator overloading'

'here elder one pay the bill'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, x):  # __gt__ method is called when > operator is used
        'for self p1 values are assigned,for x p2 values are assigned'
        if self.age > x.age:  # it will chcek who is elder
            return True
        else:
            return False


p1 = Person("ram", 10)
p2 = Person("shyam", 20)
if p1 > p2:  # here by > operator __gt__ is called
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
