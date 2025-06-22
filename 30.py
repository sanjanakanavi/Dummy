# coding exercise
'WAP to choose who will pay the bill'
import random
names = input("enter the names with comma ")
# split function is used to split elements into list
nameList = names.split(",")
print(nameList)
# 1st method
ch = random.choice(nameList)
print(f"kehooo, {ch} will pay the bill")

# 2nd method
l = len(nameList)
b = random.randint(1, l)
print(f"{b}th person will pay the price")
