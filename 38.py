# more operations on sets
set1 = {'ram', 'shyam', 'jenny'}
set2 = {'jenny', 'jiya', 'akash'}
set3 = {'ram', 'shyam', 'jenny', 'jenny', 'jiya', 'akash'}
print(set1.isdisjoint(set2))  # checking if sets are disjoint
print(set1.isdisjoint(['mohan', 'soumya']))
print(set1.issubset(set2))  # checking fro subset
print(set1.issubset(['ram', 'shyam', 'jenny', 'boss']))
print(set1 <= set2)  # subset using operator
# only one argument is possible in checking superset
print(set3.issuperset(set1))
print(set3 >= set2)  # superset using operator
set2.clear()  # clearing all elements in set
print(set2)
del set2  # it will delete the whole set ,removes from code itself
print(set2)
