# coding exercise
'check if number is prime or not'
import math
number = int(input("enter a number"))


def prime():
    is_prime = True
    if number == 1 or number == 0:
        is_prime = False
    for i in range(2, math.ceil(number/2)+1):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("number is prime")
    else:
        print("number is not a prime")


prime()
