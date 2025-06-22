# tuples in python
'it is set of collection of items with round brackets'
tuple1 = (1, 10, -15, 9, 10)
'tuples can be of all datatypes or mixed can also be created, duplicate items are allowed'
tuple2 = (1, 'sanjana', True, 10.10)
tuple3 = (10,)  # to store single item
print(type(tuple1))
print(tuple2)
'left to right indexing starts from 0 ,right to left from -1'
print(tuple2[1], tuple2[-2])
'tuples are immutable ,cannot change or add or remove the data'
print(tuple1[1:4])  # slicing can be done
print(tuple1[::2])  # skipping elements by 1
tuple4 = (30, 40, 50)
tuple5 = (60, 70, 80)
tuple6 = (tuple4, tuple5)
tuple7 = tuple4+tuple5
print(tuple6)  # nesting of tuplse
print(tuple7)  # its length is 6
print(min(tuple1), max(tuple1))  # minimum and maximum of tuple
print(tuple1.count(10))  # how many occurance of element in tuple
print(tuple1.index(10))  # to find index of first occurance of an element
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))  # converting list into tuple
print(tuple4*3)  # repeating elements of tuple
