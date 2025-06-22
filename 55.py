# dictionary in python
'dictionary is key value pair to store real world data in coding'
'syntax: dict_name={key:value}'
'dictionaries are ordered in recent version of python'
'dictionaries are mutable'
'u can add, remove, or change values in dictionaries,but keys are immutable'
'if 2 keys are same then it will consider last occured value of that key'

phone_no = {
    'ram': 1234,
    'shyam': 5678,
    'mohan': 8976
}
print(phone_no)
print(phone_no['ram'])  # to access particular key value

dict1 = dict({
    'ram': 1234,
    'shyam': 5678,
    'mohan': 8976
})  # another way to define dictionary using dict() function
print(dict1)

dict2 = dict([
    ('ram', 1234),
    ('shyam', 4567),
    ('mohan', 8976)
])  # another way to define dictionary using dict() function
print(dict2)
dict1['mohan'] = 9999  # we can change the value of keys
print(dict1)
dict1['madhav'] = {1111, 2222, 3333}  # adding another key with list of values
print(dict1)
dict1['mohan'] = {
    'mohan_home': 5555,
    'mohan_office': 7777
}  # adding another dictionary inside dictionary
print(dict1)
# accessing value from dictionary of dictionary
print(dict1['mohan']['mohan_office'])
# get() is not case sensitive it wont show error even if u enter wrong key ,it will return none
print(dict1.get('ram'))
del dict1['mohan']  # deleting an item from dictionary
print(dict1)
# another way to delete an item from dictionary and it will return the item
print(dict1.pop('ram'))
print(dict1)
dict2.popitem()
print(dict2)  # popitem() will delete last item of dictionary
dict1.clear()  # it will delete all the items from this dictionary
print(dict1)
print(dict2.keys())  # to find what all keys are present in dictionary
print(dict2.values())  # to find all the values in dictionary
print(dict2.items())  # to find items in dictionary
for i in phone_no:  # iterating dictionary
    print(i)  # this will print only keys
    print(phone_no[i])  # this will print only values
for i in phone_no.items():
    print(i)  # this method will print items in dictionaries
phone_no2 = phone_no.copy()  # this will copy items from one dictionary to other
print(phone_no2)
