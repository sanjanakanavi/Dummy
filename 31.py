# nested list
list = [10, 20, 30, [40, 50, 60], 70, 80]
print(len(list))
print(list[3])  # accessing sublist
# accessing individual sublist elements
print('', list[3][0], '\n', list[3][1], '\n', list[3][2])
print(list[-3])  # accessing sublist from backwards
# otherthan index using length function to access sublist
print(list[len(list)-3])
print(list[3][:])  # slicing,by default[index(0):length(3)]
print(list[3][0:2])  # printing only 2 sublust elements using slicing
