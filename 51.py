# types of arguments of functions in python
'''1.default
   2.positional
   3.keyword
   4.arbitrary/valuabla length
   4.a: arbitrary positional 
   4.b: arbitrary keyword'''
# simple example


def greet1(name):
    print(f"hi its me {name}")
    print("what is ur branch name?")


greet1("sanjana")
print()

'2.positional arguments'


def greet2(name, dept):  # name comes first and then dept ,orderwise(positional)
    print(f"hi its me {name}")
    print(f"are you from {dept} department?")


# position of an argument according to statements and giving inputs according to statments is important
greet2("sanjana", "EC")
print()

'3.keyword arguments: is used when u dont know functionbody'


def greet3(name, dept):
    print(f"hi its me {name}")
    print(f"are you from {dept} department?")


# specifying the keyword/parameter name to an argument which is given
greet3(name="sanjana", dept="EC")
print()
greet3("sanjana", dept="EC")  # mixture of positional and keyword arguments
print()
'rule: first positional arguments comes then keyword arguments comes'

'1.default arguments: fixed value for parameter'


def greet4(name, subject, dept="EC"):  # here dept is fixed ,so can enter only 2 arguments
    print(f"hi its me {name}")
    print(f"is {subject} is ur fav subject?")
    print(f"are you from {dept} department?")


# if we dont give 3rd argument it takes default value assigned
greet4("sanjana", "maths")
print()
# if we give 3rd argument it will update to given argument and ignores default value
greet4("sanjana", "maths", "ME")
print()
'rule: positional arguments comes first then default arguments comes'

'4.arbitrary arguments: these are used when we dont know no of parameters we want to add'

'4.a: arbitrary positional arguments :uses only one * symbol'


def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"sum is {c}")


add(1, 2, 3, 4, 5)
print()


def add1(*numbers, name):  # other way: add1(name,*numbers):u dont have to use keyword
    c = 0
    for i in numbers:
        c += i
    print(f"sum is {c}")
    print(name)


# in arbitrary u have to use keyword to give arguments for other variable or first place positional parameters then arbitrary
add1(1, 2, 3, 4, 5, name="sanjana")
print()

'4.b: arbitrary keyword arguments(kwargs)'


def info_person(*args, **kwargs):
    for key, value in kwargs.items():  # stores in the form of dictionary
        print(key, value)
    print(args)


info_person(1, 2, name="sanjana", branch="EC", age=22)
info_person(1, 2, 3, name="kartik", branch="ME")
'rule: first arbitrary positional comes then arbitrary keyword comes'
'arbitrary positional stores values in form of tuples'
