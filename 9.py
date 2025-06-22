# operators in python
"""types of operators
1.arithmetic
2.comparision
3.logical
4.bitwise
5.assignment
6.identity
7.membership"""
# +,-,*,/,% are the operators
# in division '/' the result will always be in float ,
# if we want result in whole number then we have to use // to discard reminder
print(5/2)
print(5//2)
# to get a power of a number we use **
print(12**2)
# for using multi operators we use PEMDAS rule(impotance of each operator)
# 1. ()
# 2.right to left ---> ** , if operator repeats then follow rule of associativity
# 3.left to right --->  * , / , // , %
# 4.left to right --->  + , -    it solves equation from left to right
print(5+2*3-1+10/5)

w = float(input("enter weight in kg "))
h = float(input("enter height in meters "))
bmi = w/(h**2)
print(int(bmi))
