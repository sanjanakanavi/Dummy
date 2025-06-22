import numpy as np
'matrix'
'entering data will look same as array,showing data also look same as array,but types will be diff'
v1 = np.matrix([[1, 2], [5, 6]])
print(v1)
print(type(v1))
v2 = np.matrix([[1, 2], [5, 6]])
'addition'
print(v1+v2)
'subtraction'
print(v1-v2)
'multiplication, dot() we can use'
'broadcast rules will be applied here,sometimes not'
'in some cases * multiplication works,it multiplies by the method of matrix multiplication,but not as array multiplication'
'in array multiplication,corresponding values are multiplied,this is basic diff of array and matrix'
print(v1.dot(v2))
print(np.dot(v1, v2))

'matrix functions'

'transpose,swapaxes,inverse,power,determinate'

'transpose()-> will make rows into columns and columns into rows'
v3 = np.matrix([[1, 2, 3], [4, 5, 6]])
print(np.transpose(v3))
# or
print(v3.T)

'swapaxes will also make rows into columns and columns into rows,but need to give axis1 and axis2'
print(np.swapaxes(v3, 1, 0))
'0,0/1,1-->original form,1,0/0,1-->columns wise(vertically)'

'inverse of matrix=left diagonals will be swaped,right diagonals will be made negative in case of 2D matrix'
v4 = np.matrix([[1, 2], [3, 4]])
'''
[1 2] ==  1/       [4 -2] == -1/2[4 -2]==[-2     1]
[3 4]   (1*4)-(3*2)[-3 1]        [-3 1]  [1.5 -0.5]
'''
print(np.linalg.inv(v4))


'power==a2==a.dot(a),here it will perform dot product'
'function we can use is linalg.matrix_power(matrixname,powernumber(n))'
'''n can be n=0,n<0,n>0 
when n=0 then it returns identity matrix i.e=[1 0]
                                             [0 1]
when n>0 then it will return multiplied matrix or power of matrix
when n<0 then it will return a matrix which is (inverse*power)'''
print(np.linalg.matrix_power(v4, 0))
print(np.linalg.matrix_power(v4, 2))
print(np.linalg.matrix_power(v4, -2))

'''determinate 
[a b c]
[d e f] = a[ei-hf]-b[di-gf]+c[ge-dh] 
[g h i]
''''function is linalg.det(matrixname), mostly has to be square matrix'
'if in 3D matrix 2 rows are same then determinate will be zero'
print(np.linalg.det(v4))
