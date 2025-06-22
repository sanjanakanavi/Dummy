import numpy as np
"""
need of numpy:
1. Creation of Arrays/Matrices
2. Perform several operations on arrays/matrices
3. perform integral calculus operations
4. Solving Differential equations
5. Statistics related operations etc
To perform these complex mathematical operations, python does not contain any inbuilt library.
To perform these complex operations we require a library which is nothing but numpy.

Numpy stands for: Numerical python library
numpy is developed on top of numeric library in 2005
numeric library devleoped by jim hugunin
numpy developed by travis oliphant
numpy is freeware and opensource library
numpy was written in python and c languages
numpy is super fast

numpy acts as backbone for data science libraries like pandas,scikit learn ,etc
pandas internally use 'nd array' to store data ,which is numpy data structure

numpy has vectorization feature which improves performance while iterating elements

[1 dimentional array is called vector]
[2 dimentional array is called matrix]

ndarray in numpy:[n-Dimensional arrays or numpy array]-->
-in numpy,we can hold data by using array data structure
-the arrays which are created by using numpy is called nd arrays.
-this nd arrays is most commonly used in data science libraries like pandas,scikit learn ,etc

array: an indexed collection of homogeneous elements

-numpy library contain several functions to create nd arrays and to perform several required operations
"""
"""
numpy vs traditional python code:
-the performance of numpy is too good when compared with traditional python code

"""
a = np.array([10, 20, 30])  # creating array
b = np.array([1, 2, 3])
print(a)
print(type(a))  # find type of array

'dot product:sum of products of array elements= a.b=sum(a[i] * b[i])'
'traditional python code to find dot product'


def dotproduct(a, b):
    result = 0
    for m, n in zip(a, b):
        result = result + m*n
    print("dot product: ", result)


dotproduct(a, b)

'dot product by numpy of 2 arrays, fastest method'
print(np.dot(a, b))

'in python 2 ways to create arrays'
'1.by using array module, 2.by using numpy module'
'array module is not recommended bcz there is no much library support'

'to iterate the array'
for i in a:  # a is array
    print(i)


"""
differenecs between list and numpy arrays:

-list is inbuilt data type but numpy array is not inbuilt,
to use numpy arrays,we have to install and import numpy library explicitly.

-list can hold heterogeouns (diff types)elements:
ex:list=[10,10.5,"sanjana",True]
numpy arrays can hold homogeneous elements:
ex:a=numpy.array([10,20,30])

-on arrays we can perform vector operations(the operations which can be performed on every element of the array)
but we cannod perform vector operations on list

-arrays consume less memory when compared with list
to check of size,import sys, then use sys.getsizeof() function

-arrays are super fast when compared with list

-numpy arrays are more convinient to use while performimg mathematical operations
"""
"""
creation of numpy arrays:

numpy library contains several functions to create ndarray based on our requirement.
the follwing are few of such functions:

1.array()
2.arange() #creating arrays with range
3.zeros() #creating array with zeros
4.ones()
5.linspace()
6.eye()
7.random()
etc

"""
print(a+1)  # this is vector operations ,1 is added to every element of array ,we cannot do this with list
