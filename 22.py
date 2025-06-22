# coding exercise on bmi

weight = float(input("enter ur weight"))
height = float(input("enter ur height"))
bmi = round(weight/height**2)
if bmi < 18.5:
    print(f"your bmi is {bmi} and your underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} and your normal")
elif bmi < 30:
    print(f"your bmi is {bmi} and your overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} and your obese")
else:
    print(f"your bmi is {bmi} and your clinically obese")
