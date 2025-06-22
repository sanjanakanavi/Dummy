# coding exercise
'write a program to find maximum from the list of numbers'
numbers = input("enter the numbers with space ")
numbers_list = numbers.split()
count = 0
for i in numbers_list:
    count += 1  # counting numbers
print("count:", count)
for i in range(0, count):
    # converting string elements to integers
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)
maximum_number = numbers_list[0]  # setting first element as maximum
for number in numbers_list:
    if number > maximum_number:  # logic to find maximum
        maximum_number = number
print("maximum number is :", maximum_number)
