# about modules in python

'there are 2 types of modules :bultin, user defined modules'
# print(help("modules"))code  # this will give the list of bultin modules
# print(help("math"))code  # if we want to know what is there in specific module

# (import math)code
# print(math.e)code  # accessing values /method from math module

# this will rename random as r in this module,u can fetch methods like 'r.randInt()'
# (import random as r)code

# (from math import *)code  # if we put * then it imports all the methods in math


# this is method to use 'from' keyword to extract specific method/values from that module
'if u use "from" keyword then no need to mention modulename when u use its methods/values'
'"as rdm" is used to rename method name random as rdm ,to use it further as rdm'
# (from random import random as rdm)code

'''if imported modules attribute/method names are same as attributes/mathods names present in current module 
then by default u have to use modulename before using attribute or method 
example : modulename.methodname()'''
