# break,continue and pass
'break: break statement is used to come out of the loop or break the loop at some point'
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("hi")
print("out of the loop")

list1 = ['hi', 'hello', 'welcome']
names = ['sanjana', 'krishna', 'radhe']
for item in list1:
    for name in names:
        print(item, name)
        if item == 'hello' and name == 'krishna':
            break
    print("out from the inner loop")
print("out from the outer loop")

'continue: continue wit next iteration'
'continue skips the present iteration and go for new and next iteration'
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        continue
    print("hi")
print("out of the loop")


'pass: is used to make loop or function null or an empty loop or function '
'so that u can use that loop or function in future ,pass acts as placeholder'
'means pass containig loop has nothing to do in code'
for i in range(1, 11):  # i want this loop but want to use it in future
    pass  # so we use pass to keep the loop empty
