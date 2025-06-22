# for else loop in python
'else part statements are executed only if for part is successfully executed'
tuple1 = (1, 2, 3, -4, 5, 10)
for i in tuple1:
    print(i)
else:
    print("loop completed successfully u r in else block")
'if we use break statement in for loop then else part wont get executed'
list1 = [1, 2, 3, 4, 7, 8]
for j in list1:
    if j % 6 == 0:
        print(j)
else:
    print("no number divisible by 6 in this sequence")
