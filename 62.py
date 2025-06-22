# coding exercise
'finding days in month including leap year'


def leap_year(year):  # logic to check leap year,return true or false
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):  # to return days
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30,
                 31, 30, 31]  # taking list of days in a month
    if leap_year(year) and month == 2:  # if leap_year is true and month is 2 then it returns 28
        return 29
    else:
        # else it returns suitabl value from the list
        return days_list[month-1]


year = int(input("enter the year\n"))
month = int(input("enter the month\n"))

days = days_in_month(year, month)  # storing the return value in variable
print(days)
