# Nested if, if else, elif
'example for nested if'
a = 28
if a % 2 == 0:
    print("even")
    if a > 30:
        print("greater than 30 great!!!")
print("bye")

'example for nested if else'
height = float(input("enter the height "))
if height >= 3:
    print("can ride")
    age = int(input("what is ur age "))
    if age <= 18:
        print("pay 250rs")
    else:
        print("pay 500rs")
else:
    print("sorry can't ride")
print("thankyou")

'example for nested elif'
h = float(input("enter the height "))
if h >= 3:
    print("can ride")
    a = int(input("what is ur age "))
    if a < 12:
        print("pay 150rs")
    elif a <= 18:
        print("pay 250rs")
    else:
        print("pay 500rs")
else:
    print("sorry can't ride")
print("thankyou")
