# while loop in python
'syntax:while condition:'
'            statements'
'while loop executes till while condition fails'
'while else is possible here but if while loop'
'exits from loop by break statement or forcefull termination '
'then else is not executed,else is executed only if while loop condition fails'
'when u dont know the ending point then we use while loop'
count = 1
while count <= 5:
    print(count)
    count += 1
print("out from the loop")

c = 5
while c > 0:
    print(c)
    c -= 1
else:
    print("in else block")
print("out from the loop")

# infinite loop
total = 0
# variable used to quit from loop method
number = int(input("enter a number(0 to quit)"))
while number != 0:
    total += number
    number = int(input("enter a number(0 to quit)"))
print("total is : ", total)
