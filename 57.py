# nested dictionaries
'syntax:data={key1:{dict1} , key2:{dict2}, key3:[list]}'
student_data = {
    'sanjana': {
        'roll_no': 10,
        'age': 22,
        'course': 'python'
    },
    'kartik': {
        'roll_no': 11,
        'age': 23,
        'course': 'java'
    }
}
print(student_data)
print(student_data["sanjana"])
print(student_data["kartik"]['age'])
student_data['kartik']['ph_no'] = 99999  # addign element to inner dictionary
print(student_data)
del student_data['kartik']['ph_no']  # deleting item from inner dictionary
print(student_data)

# nesting a list in dictionary
travel = {
    "gujrat": ['dwarkadish', 'somnath', 'statue of unity'],
    "rajasthan": ['jaipur', 'udaipur']
}
print(travel)
