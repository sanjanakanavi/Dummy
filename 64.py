# global keyword in python
b = 10  # its a global variable


def display():
    'we can access global variables into functions but not local to global and u cannot modify global variable in function'
    a = 15  # its a local variable which is allowed only inside function
    global b  # using global keyword we can refer to global variable then we can modify global variable inside function
    b = b+1  # if global keyword used then this expression is valid
    print(a)
    print(b)

    def ror():  # function inside function
        global c  # creating global variable inside the function
        c = 50
    ror()


display()
print(c)  # we can access global variable which is created inside the function
print()

name = "sanjana"


def display():
    global name
    name = name+" kanavi"


print(name)
display()
print(name)
