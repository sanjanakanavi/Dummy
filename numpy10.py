import numpy as np
'numpy array functions:insert and delete functions'

'insert(arrayname , indexnumber , value)'
v1 = np.array([1, 2, 3, 4, 5])
v2 = np.insert(v1, 2, 6)
print(v2)
v3 = np.insert(v1, (2, 5), 7)  # inserting value in multiple positions
print(v3)
'if u try to insert float ,it will take is as integer only'

'inserting into 2D array,u have to pass axis'
v4 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
v5 = np.insert(v4, 2, 6, axis=0)  # according to column index
print(v5)
v6 = np.insert(v4, 2, 6, axis=1)  # according to row index
print(v6)
'inserting multiple values in form of list'
# max can be 2 values to insert when rows are 2
v7 = np.insert(v4, 2, [22, 23], axis=1)
print(v7)
# max can be 4 values to insert when colunms are 4
v8 = np.insert(v4, 2, [22, 23, 24, 25], axis=0)
print(v8)

'append(arrayname,value)'
v9 = np.append(v1, 6.5)  # adds 6.5 at the end
print(v9)
'here u can insert float also'

'appending in 2D,u have give axis value'
'axis=0,no of columns=values / axis=1,no of rows=values'
v10 = np.append(v4, [[2, 3, 4, 5]], axis=0)  # passing values in a list
print(v10)

'delete(arrayname,index at what u want to delete)'
v11 = np.array([3, 4, 5, 6, 7, 8])
v12 = np.delete(v11, 3)  # deleting value at index 3
print(v12)
