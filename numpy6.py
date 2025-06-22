import numpy as np
'iterating numpy arrays'
var1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in var1:  # iterating 1 D array
    print(i)

var2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
for i in var2:  # iterating rows
    for j in i:  # iterating values in rows
        print(j)  # iterating 2 D arrays

var3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in var3:  # iterating outer rows
    for j in i:  # iterating inner rows
        for k in j:  # iterating values in rows
            print(k)  # iterating 3D arrays

'there is function nditer() which will iterate multiple dimension arrays'
for i in np.nditer(var3):
    print(i)

'in flags we can store iterated data and in op_dtypes we can give what datatype we want'
# storing in buffer in a form of string
for i in np.nditer(var3, flags=['buffered'], op_dtypes=['S']):
    print(i)

'there is a function called ndenumerate() which will return index values with data'
for i, d in np.ndenumerate(var3):
    print(i, d)  # i for index,d for data


'copy vs view in numpy arrays'
'copying data'
var4 = np.array([1, 2, 3, 4, 5])
copy = var4.copy()
print(copy)
'viweing the data'
view = var4.view()
print(view)
'''
diff between copy and view
1. copy owns the data,view doesnot owns the data
2. copy of an array is the new array,view is just the view of an original array
3.the changes made in copy doesnot reflect in original array,any changes made in view will effect the original array
and any changes made in original array will effect the view array
'''
