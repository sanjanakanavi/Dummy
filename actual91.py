'''when we create a module there will e some special variables created to it which can be seen by using dir() method
example is __name__==__main__ '''
# print(dir())  # u can see all the special variables
# print(__name__)  # in this class its value is __main__
'but when u import this module in other and run there __name__ value changes into original module name'


def display(name):
    return name


def do_something():
    print("this is doing something")


if __name__ == "__main__":  # this will not be executed in other module bcz __name__ value will be changed
    print("this is actual91")
    name = input("enter ur name")
    print(display(name))
do_something()
