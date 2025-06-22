# for loop in python
name = 'sanjana'
for i in name:
    print(i)
names = ['sanjana', 'sumangala', 'shivaling']
for j in names:
    print(j)
    if j == 'sanjana':
        print("hey its sanjana")

numbers = [1, 2, 3, 4, 5]  # printing square of all numbers
squares = []  # printing squares in list
print("squares of all numbers are:")
for k in numbers:
    square = k**2
    print(square)
    squares.append(square)
print("the list of squares is:", squares)
