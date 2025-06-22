# coding exercise
'write a program to calculate average height from a list heights'
heights = input("enter the heights with space")
height_list = heights.split(" ")
count = 0
for i in height_list:
    count = count+1  # counting the no of heights using for loop
print("count:", count)
for h in range(0, count):
    # converting heights into integers and putting in same list using range function
    height_list[h] = int(height_list[h])
print(height_list)
total = 0
for i in height_list:
    total += i  # to find sum
avg = total/count  # average
print(round(avg))
