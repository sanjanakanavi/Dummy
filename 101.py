# higher order functions
'these functions can accept function parameter '


def greet():
    print("hi")


def display(other_function):  # here for parameter we can pass a function
    print("display function")
    # if we want to execute greet after display u can write like
    # other_function()


# just passing the name of function will only execute display function but not greet
display(greet)
display(greet())  # with prenthesis it will execute greet function also


def greet_louder(name):
    print(f"hi, {name.upper()}")


def greet_softer(name):
    print(f"hi, {name.lower()}")


def hello(other_function, name1):
    print("this is hello function")
    other_function(name1)  # parameter should be same as hello(parameter)


# here we can write method name without parameter in brackets
hello(greet_louder, "sanjana")
hello(greet_softer, "sanjana")

'function can return a function lets see'


def ayodhya(name):
    print("welcome to ayodhya")

    def greet():
        print("hare krishna")

    def welcome():
        print("jai shree ram")
    if name == "sanjana":
        return greet  # returning a function
    else:
        return welcome


# storing returned function into variable
new_funct = ayodhya("sanjana")
new_funct()  # u can just call that returned function


'calculator function which accepts otherfunction and return values'


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


def calculator(function, x, y):
    # printing returned value in function itself
    print(f"result is {function(x, y)}")


calculator(mul, 5, 5)
