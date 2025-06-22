"""
array attributes:
the follwing are the array attributes:

1.ndim--to get the dimension of an array(one or two)
2.shape--to get the shape of an array(row,column in 2d) or (no of elements in 1 d)
3.size--to get size of the array whch is nothing but no of elements
4.dtype--to get the data type of array elements
5.itemsize--the size of each array element in bytes

"""
import numpy as np
'example 1'
a = np.array([10, 20, 30, 40])
print(a.ndim)  # =1
print(a.shape)  # =(4,)  # no of elements in a 1 dimension
print(a.size)  # =4
print(a.dtype)  # =int32
print(a.itemsize)  # =4

'example 2'
b = np.array([[10, 20, 30], [40, 50, 60]], dtype=float)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)

"""
in python we have datatypes like int,float,complex,bool,str,etc

but numpy has some extra datatypes in addition to these datatypes,
we can represent datatypes by using single character also:

i->integer(int8,int16,int32,int64)by default-int32
b->boolean(True,False)
u->unsigned ineteger(uint8,uint16,uint32,uint64)
f->float(float16,float32,float64)by default-float64
c->complex(complex64,complex128)
s->string
O->object
V->the fixed chunk of memories for other types
U->unicode string
M->datetime
etc

int8
the value will be represented by 8 bits
the range of values -128 to 127

int16
the value will be represented by 16 bits
the range of values -32768 to 32767
"""
'to create array of required datatype'
d = np.array([10, 20, 30, 40], dtype='i8')  # in i8, 8 is in bytes==int64
print(d.dtype)

'to convert type in existing array, we can use astype() function'
'example'
c = np.array([10, 20, 30])
print(c.dtype)  # type before converting
c = c.astype('float64')  # converting to float64
print(c.dtype)  # type after converting

'by using the corresponding data type function also,we can convert the type of array'
'example'
f = np.array([10, 20, 30, 0, 40])
print(f.dtype)  # type before converting
g = np.bool_(f)  # converting f array into boolean
print(g)  # for 0 =false,other values=true
print(g.dtype)  # after converting

'creating array using array()'
i = np.array([10, 20, 30])  # creating array
print(i)

'creating array using arange(x,y) where y is excluded and creates range of elements'
h = np.arange(1, 9)  # creates array of 1 to 8
print(h)

'creating array by taking inputs by user'
l = []  # take an empty list
for i in range(4):  # 4 elements we can put
    var = int(input("enter: "))  # taking input values and converting to int
    l.append(var)  # adding values to the list
arr = np.array(l)  # putting list into array
print(arr)  # printing an array

'''1D array-->[]
   2D array-->[[]]
   3D array-->[[[]]]
   so on '''

ar1 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]])  # 3D array
print(ar1)
print(ar1.ndim)

'to create 10 dimension array then'
ar2 = np.array([1, 2, 3, 4], ndmin=10)
print(ar2)
print(ar2.ndim)

'create array of zeros'
ar_zero = np.zeros(4)  # 1D array
ar_zero1 = np.zeros((3, 4))  # 2D array,can create n dimension array
print(ar_zero)
print(ar_zero1)

'create array of ones'
ar_ones = np.ones(4)  # 1D array
ar_ones1 = np.ones((3, 4))  # 2D array,can create n dimension array
print(ar_ones)
print(ar_ones1)

'creating an empty array,in empty array at first it will store prevoius data of memory'
ar_em = np.empty(4)  # 1D array
print(ar_em)  # it shows previous data

'creating array of range, values start from 0 ,works as range function'
ar_rn = np.arange(4)  # 0 1 2 3
print(ar_rn)

"creating array ,diagonal elements filled with 1's"
ar_eye = np.eye(3)  # creates 2D array of (3,3)
# we can specity row and colum, first 3 column will have 1 diagonal other 2 column wont have , so it will adjust by itself
ar_eye1 = np.eye(3, 5)
print(ar_eye)
print(ar_eye1)

'create an array with values that are spaced linearly in a specified interval'
'syntax= np.linspace(start range,stop range,no of elements)'
ar_lin = np.linspace(0, 20, num=5)
print(ar_lin)

# will not consider endpoint when endpoint is false
ar_lin1 = np.linspace(0, 20, num=5, endpoint=False)
ar_lin2 = np.linspace(0, 20, num=5, endpoint=True)  # will consider endpoint
# returns a tuple containing an array
ar_lin3 = np.linspace(0, 20, num=5, retstep=True)
print(ar_lin1)
print(ar_lin2)
print(ar_lin3)
