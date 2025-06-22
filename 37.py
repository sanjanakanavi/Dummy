# more methods on sets
set1 = {'ram', 'shyam', 'jenny'}
set2 = {'jenny', 'jiya', 'akash'}
set3 = {'ankur', 'pradeep'}
print(set1.difference(set2))  # finding difference method 1
print(set1 - set2)  # difference method 2
set1.difference_update(set2)  # it will update set1 by difference results
print(set1)
set1.add('jenny')
'symmetric difference = (setA union setB) - (setA intersection setB)'
# finding symmetric difference,multiple sets/arguments are not allowed method 1
print(set1.symmetric_difference(set2))
# symmetric differenec , here multiple sets are allowed method 2
print(set1 ^ set2 ^ set3)
# it will update the set after performing symmetric difference
set1.symmetric_difference_update(set2)
print(set1)
