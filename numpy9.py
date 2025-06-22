import numpy as np
'''shuffle,unique,resize,flatten,ravel functions'''

'shuffle'
v1 = np.array([1, 2, 3, 4, 5])
np.random.shuffle(v1)  # shuffling of v1 array
print(v1)

'unique:gives unique values ignoring duplicates'
v2 = np.array([1, 2, 3, 4, 2, 5, 2, 6, 2, 7])
v3 = np.unique(v2)  # gives unique values from array
print(v3)
# it will return indexes,counts/repeatations with data
v4 = np.unique(v2, return_index=True, return_counts=True)
print(v4)

'resize: can make 1d to 2d array,or whatever u want'
v5 = np.array([1, 2, 3, 4, 5, 6])
v6 = np.resize(v5, (2, 3))  # resizing by 2 rows and 3 values in each row
print(v6)

'''
flatten and ravel are used to make 2D arrays into 1D array
while using flatten and ravel functions u need to use orders:
order:{'C','F','A','K'}optional
C-->to flatten in row major(c-style) order, it consider values from left to right horizontally
F-->to flatten in column major(fortran style) order,it consider values from top to bottom vertically
A-->to flatten in column major order,if 'a' is fortran(contiguous) in memory,row major order otherwise
K-->to flatten 'a' in the order the elements occur in memory
the default is 'C'
'''
v7 = np.array([[1, 2], [3, 4], [5, 6]])
print(v7.flatten())  # 2D to 1D
print(v7.flatten(order="F"))

print(v7.ravel())  # default order=C
print(v7.ravel(order='A'))
print(v7.ravel(order='K'))
