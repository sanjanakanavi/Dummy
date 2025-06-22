# round() function
'syntax: round(number, no of digits upto where u want to roundoff)'
'number is compulsary and no of digits is optional ,if its 0 it returns integer'
print(round(7))
# if u give input number as integer it will return the int value same
print(round(7, 2))
# if u dont mention 0 ,it will return integer value after roundingoff the number
print(round(7.61))
print(round(2.6666, 2))
# if u mention no of digits as 0, it will return as float if number is in float
print(round(2.6657, 0))
'if decimal is .5 then it will return nearest even number '
print(round(7.5), round(6.5))
'if no of digits is negative ,it will return nearest multiple of 10'
'no of digits = no of digit considered to roundoff the number from right to left'
'if last digit of number is 5 then it roundoffs to the nearesrt even number'
print(round(674, 2))  # it will return integer
print(round(674, 0))  # it will also return integer bcz number is of integer type
# it return 0 bcz it consider 4 digits from right to left as 0 ,as 0000 ,so 674 vanishes
print(round(674, -4))
# it will return 660 bcz it consider last digit as 0 bcz it is -1 , and last digit is 5 it roundoff to nearest even number
print(round(665, -1))
print(round(675, -1))  # here it returns 680 bcz nearest even number is 8
print(round(-8/3))  # we can roundoff any negative numbers
print(round(-1.5))
print(round(-8/3, 2))  # it returns upto 2 decimal bcz no of digits is 2
# it will return 700 bcz in negative no of digits it will not consider numbers after decimal
print(round(674.78996, -2))
