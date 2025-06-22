import numpy as np
'search, sort, search sorted, filter functions'

'search-->search an array for a certain value and return the indexes that get a match'
v1 = np.array([1, 2, 3, 4, 2, 5, 2, 5, 6, 7])
returned_index = np.where(v1 == 2)  # finds wherever 2 is present
print(returned_index)
# whereever 0 is generated as mod value will return its indexes,can write expressions like this
v2 = np.where((v1 % 2) == 0)
print(v2)

'''search sorted array:which performs the binary search in the array,and returns the index where the specified value would be
 inserted to maintain the search order
 
 example:there is a sorted array ,u have one number which u want to place that number into that array in a correct position.
 search sorted will return that correct position's index where u can place that number
 '''
v3 = np.array([1, 2, 3, 4, 6, 7, 8])
v4 = np.searchsorted(v3, 5)  # 5 is the number i want to insert in v3
print(v4)  # will give index number where i can place 5
'u can search from right to left'
v5 = np.array([1, 2, 3, 4, 5, 6])
#              0  1  2  3  4  5  6  7  8
# search from right to insert a list
v6 = np.searchsorted(v5, [5, 6, 7], side="right")
print(v6)

'''sort array: ordered sequence is any sequence that has an order corresponding to elements
like numeric or alphabetical,ascending or descending'''
v7 = np.array([4, 2, 6, 7, 9, 1, 8])
v8 = np.sort(v7)  # sorting numeric an array
print(v8)

v9 = np.array(['a', 's', 'd', 'f'])
v10 = np.sort(v9)  # sorting alphabetic array
print(v10)

v11 = np.array([[3, 2, 1], [6, 5, 4]])
v12 = np.sort(v11)  # sorting 2D array,values will be sorted
print(v12)

'''filter array: getting some elements out of an existing array and creating a new array out of them
here u need to pass a list containing true / false, wherever there is true it will take those values and create another array'''
v13 = np.array(['s', 'a', 'n', 'j', 'u'])
f = [False, True, True, False, True]  # true/false list
v14 = v13[f]  # passing list into that array from where we want values
print(v14)  # this is a new filter array
