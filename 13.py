# identity operators
'in python if 2 or more variables have same data or datatype ojects then the memory location of both variable will be same because it reuses'
'the memory of data if variables have same data, so 1 memory location can be accessed by many variables if it claims same data '
a, b, c = 5, 5, '5'
print(id(a))  # id() function can be used to fetch the memory address of an object
'there are 2 identity operators : is , is not'
'1. is -> it will see if 2 variables have same memory location ,if it is same then it returns true else false'
print(a is b)
"""2. is not -> it will see if 2 variables have different memory address or we can say 2 different objects then it returns true ,if same memory address
it returns false"""
print(a is not c)
