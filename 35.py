# sets in python
'used to store multiple items in a single variable in curly bracets'
'in sets duplicates are not allowed'
set1 = {1, 10, 'sanjana', 1.11, 53}  # mixed datatype is allowed
set2 = {10, 20, 30, 40, 50, 60, 70, 80}  # can be of same datatypes
print(set2)  # output can be shuffled ,there is no order in sets
'indexing on sets are not allowed bcz they are unordered'
'set elements are unchangable ,means cant replace values of items in sets'
'we can add and remove the items in sets'
'in sets boolean true and 1 are considered as same so they behave like duplicates'
set3 = set()  # to create an empty set,need to use set() function
print(set3)
print(type(set1))  # finding type of inbuilt datatype
set2.add(90)  # adding one item at a time to set1
print(set2)
print(len(set2))  # length of the set
set2.remove(90)  # removing an element from set
print(set2)
# discard also remove element from set, if that element is not there in set then it prints set as it is
set1.discard(1.11)
print(set1)
set1.clear()  # clearuing the set
print(set1)
print(set2.pop())  # it will remove one random item from set and also returns it
print(set2)
set2.add((1, 2, 3))  # adding tuple into set,but cannot add list in same way
print(set2)
