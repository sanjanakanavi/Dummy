import numpy as np
'numpy arithmetic operations'
'''
a+b     np.add(a,b)
a-b     np.subtract(a,b)
a*b     np.multiply(a,b)
a/b     np.divide(a,b)
a%b     np.mod(a,b)
a**b    np.power(a,b)
1/a     np.reciprocal(a)-returns array divided by 1
'''
var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
varadd = var1+3  # adding 3 directing to array
varadd1 = var1+var2  # adding 2 arrays directly
varadd2 = np.add(var1, var2)  # adding 2 arrays by function
print(varadd)
print(varadd1)
print(varadd2)

var3 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])  # 2D arrays
var4 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
varadd3 = var3+var4  # adding 2D arrays
print(varadd3)

'''
np.min(x)
np.max(x)
np.argmin(x)-gives position of min value
np.argmax(x)-gives position of max value
np.sqrt(x)
np.sin(x)
np.cos(x)
np.cumsum(x)-[1   2      3]
            =[1 1+2=3 3+3=6]
'''
var5 = np.array([1, 2, 3, 4, 5, 3, 2])
print(np.min(var5))  # minimum of array
print(np.max(var5))  # maximum of array
print(np.argmin(var5))  # position of min
print(np.argmax(var5))  # position of max
print(np.sqrt(var5))  # find the squareroot of array
print(np.sin(var5))  # finds the sin value of array
print(np.cos(var5))  # finds the cos value of array
print(np.cumsum(var5))  # finds the cumulative sum of an array

'in 2D array we have to pass 2 parameters,array and axis, axis=0=column, axis=1=row'
var6 = np.array([[2, 1, 3], [9, 5, 6]])
print(np.min(var6, axis=0))  # according to column will find min
print(np.min(var6, axis=1))  # according to row will find min
