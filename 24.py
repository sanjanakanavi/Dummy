# multiple if statements coding exercise
height = float(input("enter the height "))
bill = 0
if height >= 3:
    print("can ride")
    age = int(input("what is ur age "))
    if age < 12:
        bill = 150
        print("ticketprice 150rs")
    elif age <= 18:
        bill = 250
        print("ticketprice 250rs")
    else:
        bill = 500
        print("ticketprice 500rs")
    photo = input("want a photo yes or no ")

    if photo == 'yes':
        bill += 50
    print(f"your total bill is {bill} ,thankyou")
else:
    print("sorry can't ride")
