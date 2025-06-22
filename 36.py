# operations on sets
set1 = {'sanjana', 'shreya', 'ram'}
set2 = {'ram', 'kartik', 'krishna'}
set3 = {'ankur', 'pradeep', 'ram'}
# union of sets method 1,here argument can be other than set also
print(set1.union(set2, set3))
print(set1 | set2 | set3)  # union of sets method 2, here argument is only sets
set1.update(set2)  # updating the set method 1
print(set1)
set1.update(['sanju', 'suma'])  # argument can be list tuple anything
print(set1)
set3 |= set2  # updating the set method 2
print(set3)
print(set1.intersection(set2))  # intersection of sets method 1
print(set1 & set2)  # intersection of sets method 2
'for functions we can pass any argument but in operators we can pass only sets'
set4 = {1, 2, 3, 4, 5}
set5 = {4, 5, 6, 7, 8}
# it will find intersection of 2 sets and replace set2 by those elements i.e updating the set
set4.intersection_update(set5)
print(set4)
