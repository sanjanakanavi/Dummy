# pizza order program exercise
size = input("enter the size of pizza 'small','medium','large'")
bill = 0
if size == 'small':
    bill += 100
    print("small pizza price is 100rs")
elif size == 'medium':
    bill += 200
    print("medium pizza price is 200rs")
else:
    bill += 300
    print("large pizza price is 300rs")
pep = input("do u want peporoni on ur pizza")
if pep == 'yes':
    if bill == 100:
        bill += 30
    else:
        bill += 50
cheese = input("do u want extra cheese on ur pizza")
if cheese == 'yes':
    bill += 20
print(f"thankyou ur pizza is ready,total price is {bill}")
