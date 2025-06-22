# project 6 : calculator
import os


def add(a, b):  # functions to calculate
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}  # items to choose one of them


def calculator():  # function for calculator
    number1 = float(input("enter first number\n"))  # taking input of number 1
    for symbol in operations_dict:
        print(symbol)  # asking to choose one of these
    continue_flag = True  # condition to enter while loop
    while continue_flag:
        op_symbol = input("pick an operation\n")
        # taking input for second number
        number2 = float(input("enter second number\n"))
        # according to input extracting function name
        calculator_function = operations_dict[op_symbol]
        # passing arguments to function present in it
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")  # printing result
        # asking if want to continue/new start/exit
        should_continue = input(
            "enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit").lower()
        if should_continue == 'y':  # if yes to continue
            number1 = output  # first number will be previous output,will enter while loop
        elif should_continue == 'n':  # if new start,
            continue_flag = False  # disable the while loop
            os.system('cls')  # clear the output screen
            calculator()  # call itself,so that function start from first without considering while loop
        else:  # to exit
            continue_flag = False  # disable while loop
            print("bye")  # say bye


calculator()  # calling whole function
