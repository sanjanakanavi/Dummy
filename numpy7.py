import numpy as np
'join and split functions in numpy arrays'
'''
join array->putting contents of 2 or more arrray in a single array

'''
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
v3 = np.concatenate((v1, v2))  # concatenating 2 1D arrays
print(v3)
'while concatenating 2 D arrays,need to give axis,column=0,row=1'
v4 = np.array([[1, 2], [3, 4]])
v5 = np.array([[5, 6], [7, 8]])
v6 = np.concatenate((v4, v5), axis=1)  # concatenating 2 D arrays by rows
print(v6)
# concatenating by columns,adds as new rows
v7 = np.concatenate((v4, v5), axis=0)
print(v7)

'stack functions merges arrays according to axis,merging 1D arrays to 2D arrays,3Darrays'
# merges corresponding values in rows
v8 = np.stack((v1, v2), axis=1)
print(v8)  # [[1 5]
#             [2 6]
#             [3 7]
#             [4 8]]
# merges corresponding values in columns
v9 = np.stack((v1, v2), axis=0)
print(v9)  # [[1 2 3 4]
#             [5 6 7 8]]
v10 = np.vstack((v1, v2))  # according to columns,same as stack axis=0
print(v10)  # [[1 2 3 4]
#              [5 6 7 8]]
v11 = np.dstack((v1, v2))  # according to height,1D to 3D,same as stack axis=1
print(v11)  # [[[1 5]
#               [2 6]
#               [3 7]
#               [4 8]]]
v12 = np.hstack((v1, v2))  # according to rows
print(v12)  # [1 2 3 4 5 6 7 8]


'splitting arrays :breaks one array into multiple, array_split(array,no of arrays u want)'
v13 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
v14 = np.array_split(v13, 4)  # splitting into 4 arrays
print(v14)
print(type(v14))  # it will be in the type of list
# extracting 1st array of splitted array/taking elements from list according to indexing
print(v14[0])

'splitting of 2D array'
v15 = np.array([[1, 2], [3, 4], [5, 6]])
v16 = np.array_split(v15, 3)
print(v16)
v17 = np.array_split(v15, 3, axis=1)  # splitting according to rows
print(v17)
