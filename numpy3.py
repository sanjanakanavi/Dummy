import numpy as np
'create numpy arrays with random numbers'
'rand()--> random numbers from 0 to 1'
'randn()-->used to generate random value close to 0,it can be -ve or +ve'
'''ranf()-->function for doing random sampling in numpy,returns an array of specified shape and
 fills it with random floats between 0.0 to 1.0 in a half open interval[0.0,1.0),1.0 is excluded'''
'randint()-->used to generate random number between a given range'
var1 = np.random.rand(4)  # 1D array
var2 = np.random.rand(3, 5)  # 2D array
print(var1)
print(var2)

var3 = np.random.randn(4)  # 1D array returns 4 values
print(var3)

var4 = np.random.ranf(4)  # ranf function
print(var4)

# randint function(min,max,no of elements),unarranged,can have duplicates
var5 = np.random.randint(1, 10, 10)
print(var5)

'shape and reshaping in numpy arrays'
'shape is about dimansions (row,column)'
var6 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(var6.shape)  # gives the shape of array

'to create 4 dimension array then'
var7 = np.array([1, 2, 3, 4], ndmin=4)  # changing the shape by ndim
print(var7)
print(var7.ndim)  # gives the no of dimensions
print(var7.shape)  # to find shape of an array

'to reshape 1d to 2D'
var8 = np.array([1, 2, 3, 4, 5, 6])  # 1D array
var9 = var8.reshape(3, 2)  # reshaping into 3 rows 2 columns, 2D array
print(var9)

'to reshape from 1D to 3D'
var10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
var11 = var10.reshape(2, 3, 2)  # shaping into 3D
print(var11)
'to reshape from 3D to 1D(reverse)'
var12 = var11.reshape(-1)  # var11=3D array,(-1) will make array to 1D
print(var12.ndim)  # gives dimension
