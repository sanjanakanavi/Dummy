import numpy as np
'broadcasting of numpy arrays'

'broadcast error happens when u dont match shape of the 2 arrays'

''' to perform bradcast operation,there are rules
1.same dimension
2.it should have either of the column as 1,then only it works
3.should have same no of row or column like, rows=columns or columns= rows,ex-(3,1)(1,3)
it can be one of same among row= row or column= column(2,1)+(2,3)=(2,3)here row is same,so one of the colunm should be 1

   if(1,3)(1,4)=error,bcz when u have same rows,one of the column should be 1 ,then it select max of colunms 
it will create new shape array,by taking max value of both the array shapes like among corresponding columns and rows(1,3)and (3,1)
it will create(3,3)
'''

var1 = np.array([1, 2, 3])  # (1,3)
var2 = np.array([[1], [2], [3]])  # (3,1)
print(var1+var2)  # gives (3,3) array

'indexing and slicing'
'''1D array indexing=[1 , 2, 3, 4]
                      0   1  2  3
    negative indexing -4 -3 -2 -1   
'''
var3 = np.array([1, 3, 5, 7, 9])
print(var3[3])  # extracting specific value from array by index
print(var3[-3])  # extracing value from negative index

var4 = np.array([[9, 8, 7], [4, 5, 6]])  # 2D array
print(var4[0, 1])  # first row second value,indexing in 2D array

var5 = np.array([[[1, 2], [1, 2]], [[1, 2], [1, 2]]])  # 3D array
print(var5[0, 1, 1])  # indexing in 3D array


'slicing numpy arrays'
'ability to extract any sub part of an array'
'[start:stop:step] put index values from start  to end point,where endpoint is excluded'
'gives step value for skipping of values intervally,by default it will be 1'
var6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 1D array
print(var6[2:])  # from index 2 to end slicing
print(var6[1:7])  # from values 2 to 7
print(var6[:5])  # from start to value 5
print(var6[::2])  # from start to end with skipping of single values

var7 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 3, 4, 5]])  # 2D array
print(var7[1, 1:5])  # first give row num,then slicing
