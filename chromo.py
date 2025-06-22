# 'squareroot'
# import math
# n = 8
# for i in range(1, n):  # method 1
#     if i**2 == n:
#         print(i)
# print(math.sqrt(n))  # method 2
# print(n**0.5)  # method 3

# print()

# 'area of triangle by base and height'
# base = int(input("enter base in cm"))
# height = int(input("enter height in cm"))
# area = 0.5*base*height
# print(area)

# print()

# 'swap of 2 numbers'
# a = input("enter first no")
# b = input("enter second no")
# temp = a
# a = b
# b = temp
# print(a, b)

import re
import time
'prime no'
# k = int(input("enter a prime num "))
# c = 0
# for i in range(1, k+1):
#     if k % i == 0:
#         c += 1
# if c == 2:
#     print("prime")
# else:
#     print("not prime")

'count prime from 100 to 200'
# c = 0
# L = []
# for n in range(100, 201):
#     c = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             c += 1
#     if c == 2:
#         L.append(n)
# print(len(L))
# print(L)

'factorial'
# n = int(input("enter a num for factorial"))
# total = 1
# for i in range(1, n+1):
#     total *= i
# print(total)  # method 1
# print(math.factorial(n))  # method 2

'fibonacci'
# n1 = 0
# n2 = 1
# for i in range(1, 21):
#     sum = n1+n2
#     print(n1)
#     n1 = n2
#     n2 = sum

'sum of natural nos'
# sum = 0
# for i in range(1, 26):
#     sum += i
# print(sum)

'reverse of a string'
# s = "sanjana"
# rev = s[::-1]
# print(rev)#method1

# list1 = list(s)#method2
# s1 = ""
# for i in list1[::-1]:
#     s1 += i
# print(s1)

'find dupplicates of list and count occurances'
# my_list = [5, 5, 5, 4, 3, 2, 1, 6, 7, 2, 3, 4, 9, 1]
# unique_list = []
# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)  # till here to remove duplicates
#     else:
#         print(f"{item} occured {my_list.count(item)} times")
# print(f"{unique_list} is unique list")

# 'method 2'
# my_list1 = [1, 2, 3, 4, 2, 3, 5, 5, 5, 5, 1]
# my_list2 = [1, 2, 3, 4, 2, 3, 5, 5, 5, 5, 1]

# for i in my_list1:
#     c = 0
#     my_list2_copy = my_list2.copy()  # Make a copy of my_list2
#     for j in my_list2_copy:
#         if i == j:
#             c += 1
#             my_list2.remove(j)
#     if c > 1:
#         print(i, c)

# 'method 3'
# my_list1 = [1, 2, 3, 4, 2, 3, 5, 5, 5, 5, 1]
# my_list2 = [1, 2, 3, 4, 2, 3, 5, 5, 5, 5, 1]

# for i in range(0, len(my_list1)):
#     c = 0
#     for j in range(0, len(my_list2)):
#         if my_list1[i] == my_list2[j]:
#             c += 1
#             my_list2[j] = 0
#     if c > 1:
#         print(my_list1[i], c)

'binary search'
# target = 10
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# start = 0
# end = len(list1)-1
# while start <= end:
#     mid = round((start+end)/2)
#     if target == list1[mid]:
#         print("element found")
#         break
#     elif target > list1[mid]:
#         start = mid+1
#     else:
#         end = mid-1

'add numbers in string'
# s = " Hihl44oemfkewf55mjfn858"
# num = list(s)
# result = 0
# for i in num:
#     if i.isnumeric():
#         i = int(i)
#         result += i
# print(result)

'frequency of an array'
# s = 'sanjana'
# s1 = list(s)
# dict1 = {}
# for i in s1:
#     if i not in dict1.keys():
#         dict1[i] = s1.count(i)
# print(dict1)

'find max of list'
# lis = [600, 33, 44, 67, 200, 587]
# max = 0
# for i in lis:
#     if i > max:
#         max = i
# print(max)

'patterns'


# def print_square(n):
#     for i in range(n):
#         for j in range(n):
#             # Change "" to any character you want for the square
#             print("*", end="  ")
#         print()


# # Example: printing a square of size 5
# print_square(5)
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == 1 or j == 1 or i == 5 or j == 5:
#                 # Change "" to any character you want for the square
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()


# # Example: printing a square of size 5
# print_square(5)
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j or i+j == n+1:
#                 # Change "" to any character you want for the square
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()


# # Example: printing a square of size 5
# print_square(5)
# *       *
#   *   *
#     *
#   *   *
# *       *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j or i+j == n+1 or i == 1 or j == 1:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()


# # Example: printing a square of size 5
# print_square(5)
# *  *  *  *  *
# *  *     *
# *     *
# *  *     *
# *           *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == round(n/2)+1 or j == n or j == 1:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()


# # Example: printing a square of size 5
# print_square(9)
# *                       *
# *                       *
# *                       *
# *                       *
# *  *  *  *  *  *  *  *  *
# *                       *
# *                       *
# *                       *
# *                       *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j == round(n/2)+1 or i == 1:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()


# # Example: printing a square of size 5
# print_square(9)
# *  *  *  *  *  *  *  *  *
#             *
#             *
#             *
#             *
#             *
#             *
#             *
#             *

# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j or i+j == n+1 or j == 1 or j == n:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()


# print_square(5)
# *           *
# *  *     *  *
# *     *     *
# *  *     *  *
# *           *


# def print_square(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j or i+j == n+1 or i == round(n/2) or j == round(n/2):
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()


# print_square(7)
# *        *        *
#    *     *     *
#       *  *  *
# *  *  *  *  *  *  *
#       *  *  *
#    *     *     *
# *        *        *

# def print_square(n):
#     n1 = 1
#     n2 = n*2-1
#     for i in range(1, n+1):
#         for j in range(1, n2+1):
#             if j >= n1 and j <= n2:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 += 1
#         n2 -= 1


# print_square(8)
# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *  *  *  *
#       *  *  *  *  *  *  *  *  *  *  *
#          *  *  *  *  *  *  *  *  *
#             *  *  *  *  *  *  *
#                *  *  *  *  *
#                   *  *  *
#                      *


# def print_square(n):
#     n1 = 1
#     n2 = n*2-1
#     for i in range(1, n+1):
#         for j in range(1, n2+1):
#             if j == n1 or j == n2 or i == 1:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 += 1
#         n2 -= 1


# print_square(8)
# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#    *                                   *
#       *                             *
#          *                       *
#             *                 *
#                *           *
#                   *     *
#                      *


# def print_square(n):
#     n1 = n
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n*2):
#             if j >= n1 and j <= n2:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 -= 1
#         n2 += 1


# print_square(8)
#                      *
#                   *  *  *
#                *  *  *  *  *
#             *  *  *  *  *  *  *
#          *  *  *  *  *  *  *  *  *
#       *  *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

# def print_square(n):
#     n1 = n
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n*2):
#             if j == n1 or j == n2 or i == n:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 -= 1
#         n2 += 1


# print_square(8)
#                      *
#                   *     *
#                *           *
#             *                 *
#          *                       *
#       *                             *
#    *                                   *
# *  *  *  *  *  *  *  *  *  *  *  *  *  *  *


# def print_square(n):
#     n1 = 1
#     n2 = 1
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j == n1 or j <= n2:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n2 += 1


# print_square(8)
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# *  *  *  *  *  *
# *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *


# def print_square(n):
#     n1 = n
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j == n2 or j >= n1:
#                 # Change "" to any character you want for the square
#                 print("*   ", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 -= 1


# print_square(5)
#             *
#          *     *
#       *     *     *
#    *     *     *     *
# *     *     *     *     *


# def print_square(n):
#     n1 = n
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j == n2 or j >= n1:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 -= 1


# print_square(5)
#             *
#          *  *
#       *  *  *
#    *  *  *  *
# *  *  *  *  *

# def print_square(n):
#     n1 = 1
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j >= n1 or j == n2:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 += 1


# print_square(8)
# *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *
#       *  *  *  *  *  *
#          *  *  *  *  *
#             *  *  *  *
#                *  *  *
#                   *  *
#                      *

# def print_square(n):
#     n1 = 1
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j >= n1 or j == n2:
#                 # Change "" to any character you want for the square
#                 print("*   ", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n1 += 1


# print_square(8)
# *     *     *     *     *     *     *     *
#    *     *     *     *     *     *     *
#       *     *     *     *     *     *
#          *     *     *     *     *
#             *     *     *     *
#                *     *     *
#                   *     *
#                      *

# def print_square(n):
#     n1 = 1
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j == n1 or j <= n2:
#                 # Change "" to any character you want for the square
#                 print("*", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         n2 -= 1


# print_square(8)
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *
# *  *  *  *  *  *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *


# def print_square(n):
#     n1 = n
#     n2 = n
#     for i in range(1, n*2):
#         for j in range(1, n+1):
#             if j >= n1 or j == n2:
#                 # Change "" to any character you want for the square
#                 print("*   ", end="  ")
#             else:
#                 print(" ", end="  ")
#         print()
#         if i < n:
#             n1 -= 1
#         else:
#             n1 += 1


# print_square(5)
#             *
#          *     *
#       *     *     *
#    *     *     *     *
# *     *     *     *     *
#    *     *     *     *
#       *     *     *
#          *     *
#             *


# import re
# 'adding numbers from string'
# 'input=sdf32tdsk10nmk'
# 'output=32+10=42'
# 'method 1 '
# s1 = 'sdf32tdsk10nmk'
# numbers = re.findall(r'\d+', s1)
# total_sum = sum(int(num) for num in numbers)
# print(total_sum)

'method 2 '
# s1 = 'xshjn45ndm10bnm5vb5'
# num = ''
# total = 0
# for i in s1:
#     if i.isdigit():  # if i is number then it will add to num
#         num += i
#     else:  # if num is present then it will add to total
#         if num:
#             total += int(num)
#             num = ''  # emptying after addition of num to total once
# if num:  # in string if there is number at last it will add to total
#     total += int(num)
# print(total)


# 'make string upper case'
# s1 = 'aqy23Sjh5bv78'
# print(s1.upper())


'pop first and last alphabet from string and print'
# s1 = 'sanjana'
# while s1:
#     print(s1)
#     s1 = s1[1:-1]

'CHROMOSIS '
# 'to print numbers occured more than once'
# list1 = [1, 2, 3, 4, 4, 6, 6].sort()
# set1 = set()
# for i in list1:
#     if list1.count(i) > 1:
#         set1.add(list1[i])
# print(set1)

# 'find dupplicates of list and count occurances'
# my_list = [5, 5, 5, 4, 3, 2, 1, 6, 7, 2, 3, 4, 9, 1]
# unique_list = []
# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)  # till here to remove duplicates
#     else:
#         print(f"{item} occured {my_list.count(item)} times")
# print(f"{unique_list} is unique list")

'method 2'
my_list1 = [1, 2, 3, 4, 2, 3, 5, 5, 5]
my_list2 = [1, 2, 3, 4, 2, 3, 5, 5, 5]
for i in my_list1:
    c = 0
    my_list2_copy = my_list2.copy()  # Create a copy of my_list2
    for j in my_list2_copy:
        if i == j:
            c += 1
            my_list2.remove(j)
    if c > 1:
        print(c, i)

# 'printing duplicate number and sequence value in place of it'
# list1 = [1, 2, 3, 4, 4, 6, 6, 6]
# list1.sort()
# unique_list = []
# for item in list1:
#     if item not in unique_list:
#         unique_list.append(item)  # till here to remove duplicates
#     else:
#         print(f"{item} occured {item+1} is missing number")
# print(f"{unique_list} is unique list")
# 'ida only one number 2 times repeat agidra ashta work agutta'

'string into list of words'
# str1 = "You must be the change you wish to see in the world"
# resultlist = []
# word = ""
# for i in range(0, len(str1)):
#     if str1[i] != " ":
#         word += str1[i]
#     else:
#         if word:
#             resultlist.append(word)
#             word = ""
# if word:
#     resultlist.append(word)
# print(resultlist)


'''Input : "Hello
outpu:
h=1
e=1
l=2
0=1'''
# str1 = "hello"
# frequency = {}

# # Counting the frequency of each character in the string
# for char in str1:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# # Printing the frequency of each character
# for char, count in frequency.items():
#     print(char, count)

'input=hello hi bye welcome'
'output2:hello hi bye emoclew'
# str1 = "hello hi bye welcome"
# strlist = str1.split(" ")
# word = strlist[len(strlist)-1]
# revword = ""
# for i in word:
#     revword = i+revword
# strlist[len(strlist)-1] = revword
# result = " ".join(strlist)
# print(result)


'input=hello hi bye welcome'
'output=emoclew  bye ih hello'
# str1 = "hello hi bye welcome"
# strlist = str1.split(" ")
# strlist.reverse()
# length = len(strlist)
# for i in range(0, length):
#     word = ""
#     if i % 2 == 0:
#         for j in strlist[i]:
#             word = j+word
#             strlist[i] = word
# result = " ".join(strlist)
# print(result)

'''Input :hello 1 bye  18 hi 88
output :26'''
# str1 = "hello 1 bye  18 hi 88"
# result = re.findall(r'\d', str1)
# resutl1 = sum(int(num) for num in result)
# print(resutl1)

'''I/P:Hello13@HI&byE123
O/P:hELLO13@hi&BYe123'''
# str1 = "Hello13@HI&byE123"
# result = ""
# for i in str1:
#     if i.isalpha():
#         if i.isupper():
#             i = i.lower()
#             result += i
#         else:
#             i = i.upper()
#             result += i
#     else:
#         result += i
# print(result)

'ascii conversion'
# str1 = "a"
# print(chr(ord('a')-32))

'''I/P:759
O/P:975;'''
# num = 759
# listy = []
# while num != 0:
#     num1 = 0
#     num1 = num % 10
#     num = num//10
#     listy.append(num1)
# listy.sort(reverse=True)
# result = 0
# for i in listy:
#     result = result*10+i
# print(result)


'bracket matching'
'input=((()))'
# input = ")))((([]"
# count = 0
# for i in input:
#     if i == '(' or i == '[':
#         count += 1
#     elif i == ')' or i == ']':
#         count -= 1
# if count == 0:
#     print("bracket matching")
# else:
#     print("not matched")


'another method to reverse a string'
# str1 = "sanjana"
# result = "".join(reversed(str1))
# print(result)

'to print current time'
'import time'
# currenttime = time.localtime(time.time())
# print("Current time is", currenttime)


'''
match term:
   case pattern-1:
   action-1
   case pattern-2:
   action-2
   case pattern-3:
   action-3
   case _:
   action-default
   _ refers to default case, similar to switch actions
'''

'''
The Walrus Operator allows you to assign a value to a variable within an expression. This can be useful when you need to use a value 
multiple times in a loop, but don't want to repeat the calculation.

The Walrus Operator is represented by the `:=` syntax and can be used in a variety of contexts including while loops and if statements.

'''
# names = ["Jacob", "Joe", "Jim"]

# if (name := input("Enter a name: ")) in names:
#     print(f"Hello, {name}!")
# else:
#     print("Name not found.")


'linear search'
'input:Array: [5, 8, 3, 9, 12, 7, 10]'
'Target Value: 7'
# input = [5, 8, 3, 9, 12, 7, 10]
# target = 7
# for i in input:
#     if target == i:
#         print("found")
# #method 2
# if target in input:
#     print("found")
# else:
#     print("not found")

'binary search'
'Sorted Array: [2, 4, 7, 9, 12, 15, 18, 22, 25]'
'Target Value: 7'
# input = [2, 4, 7, 9, 12, 15, 18, 22, 25]
# target = 7
# n1 = 0
# n2 = len(input)-1
# while n1<=n2:
#     mid=(n1+n2)//2
#     if target > input[mid]:
#         n1 = mid+1
#     elif target < input[mid]:
#         n2 = mid-1
#     elif target == input[mid]:
#         print("found")
#         break
# else:
#     print("not found")


'buble sort'
'input:Unsorted Array: [7, 2, 5, 1, 9, 3]'
# input = [7, 2, 5, 1, 9, 3, 0, 4]
# for i in range(0, len(input)):
#     for j in range(0, len(input)-1-i):
#         if input[j] > input[j+1]:
#             input[j], input[j+1] = input[j+1], input[j]
# print(input)

''
