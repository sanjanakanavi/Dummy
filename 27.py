# lists in python
'Its a collection of things where we can store different data types and dinamically stored means no fixed size'
'lists are mutable ,can change values,can add elements,can remove elements,lista are ordered'
numbers = [10, 0, -1, 7, 8, 9, -67, 10]  # duplicates are allowed in list
names = ['sanju', 'chiku', 'krishna']
mixlist = [1, 'sanju', True, 10.10]
print(numbers, names, mixlist)
print(numbers[1])  # accessing specific element
print(len(numbers))  # length of list
# negative indexing can be done,for negative index start from last element from -1
print(numbers[-1], numbers[-2])
# numbers[index:length] is called slicing of list,if we dont mention anything then index=0 and length=how many elements
print(numbers[1:5])
# 2 indicates no of elements get skipped means 2nd length of index it prints upto 5th length,its called extended slicing
print(numbers[0:5:2])
numbers.sort()  # sorting the list,cannot apply on mixed list
print(numbers)
numbers.reverse()  # reversing the list
print(numbers)
print(max(numbers))  # return maximum number
print(min(numbers))  # return minimum number
# append adds a single element at the end of the list at time
numbers.append((45))
print(numbers)
# insert (at what index want to add, what u want to add) for a specific
numbers.insert(2, 30)
print(numbers)
# (extend) to add multiple elements at a time in list at the end
numbers.extend([20, 40, 50, 60])
print(numbers)
numbers[6] = 77  # changing the value of element
print(numbers)
numbers[1:4] = [60, 60, 60]  # replace values of specific sublist[index:length]
print(numbers)
# removing value of element,if more same elements are there ,then it removes first occurance of element
numbers.remove(-1)
print(numbers)
# pop function will remove last element of the list
print(numbers.pop())  # this will return which element is removed
print(numbers)
# pop can remove any element by mentioning index in bracket
print(numbers.pop(5))  # this will return 5th element which is removed from list
print(numbers)
print(numbers.count(60))  # calculating repeatations of value
print(numbers.clear())  # it will clear the list and make it empty
