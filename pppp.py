# from collections import Counter
# 'remove duplicates and give repeated numbers'
# l1 = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6,]
# unique_list = []
# repeated = []
# for item in l1:
#     if item not in unique_list:
#         unique_list.append(item)
#     elif item not in repeated:
#         repeated.append(item)
# print(unique_list, repeated)

# '''a man clibing tree of 26 m  for every even sec
#   he climbs 5m and for every odd sec he drop 2 m then
#   at what time he will reach his destination'''
# '''
# 1=-2
# 2=3
# 3=1
# 4=6
# 5
# 6=9
# 7
# 8=12
# 9
# 10=15
# 11
# 12=18
# 13
# 14=21
# 15
# 16=24
# 17
# 18=27
# '''
# ' he reaches within 17 to 18 sec'

# '''a man clibing tree of 26 m  for every odd sec
#   he climbs 5m and for every even sec he drop 2 m then
#   at what time he will reach his destination'''
# '''
# 1=5
# 2=3
# 3=8
# 4=6
# 5
# 6=9
# 7
# 8=12
# 9
# 10=15
# 11
# 12=18
# 13
# 14=21
# 15=26
# '''
# 'he reaches at 15th sec'

# 'above problem in coding'


# class DestinationFinder:
#     def main():
#         target_destination = 26
#         current_destination = 0
#         for time in range(1, 27):
#             if time % 2 == 1:
#                 current_destination += 5
#             else:
#                 current_destination -= 2
#             print("Step", time, ":", current_destination)
#             if current_destination == target_destination:
#                 print("Target destination reached at time", time)
#                 break


# DestinationFinder.main()


# 'input:kartik|output:first remove 1st letter then last letter and print'
# input = 'sanjana'
# print(input)
# while input != '':
#     input = input[1:]
#     print(input)
#     input = input[:len(input)-1]
#     print(input)


# '''String s="Hello120Bye240hi60
# Output:420'''
# s = "Hello120Bye240hi600"
# total = 0
# num = ''
# for i in s:
#     if i.isdigit():
#         num += i
#     else:
#         if num:
#             total += int(num)
#             num = ''
# if num:
#     total += int(num)
# print(total)

# 'method 2'
# # import re
# # numbers = re.findall(r'\d+', s)
# # total_sum = sum(int(num) for num in numbers)
# # print(total_sum)


# 'input:153 output=1^3+5^3+3^3'
# number = 370
# numlist = []
# while number != 0:
#     num = number % 10
#     number = number//10
#     numlist.append(num)
#     num = 0
# numlist.reverse()
# print(numlist)
# total = 0
# length = len(numlist)
# for i in numlist:
#     total += (i**length)
# print(total)


# 'method 2'
# number1 = 370
# length1 = len(str(number1))
# total1 = 0
# while number1 != 0:
#     num1 = number1 % 10
#     total1 += num1 ** length1
#     number1 = number1 // 10
# print(total1)


# 'if in word vowels are odd then score+1 ,if even then score+2'
# st1 = 'programming is awesome'
# vowels = ['a', 'e', 'i', 'o', 'u']
# score = 0
# stlist = st1.split(" ")
# for i in stlist:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1
#     if count % 2 == 0:
#         score += 2
#     else:
#         score += 1
# print(score)

# '1222311 output=(1, 1) (3, 2) (1, 3) (2, 1)'
# 'use = from collections import Counter'
# numbery = 1222311
# digit_counts = Counter(str(numbery))
# output = ""
# for digit, county in digit_counts.items():
#     output += f"({digit}, {county}) "

# print(output.strip())


# 'reverse number'
# a = 12345
# revrese = 0
# while a != 0:
#     reminder = 0
#     reminder = a % 10
#     revrese = (revrese*10)+reminder
#     a = a//10
# print(revrese)


# 'find longest conjecutive length in list'
# list1 = [0, 3, 7, 2, 5, 8, 4, 6, 1, 100, 101]
# len_con = 1
# for i in list1:
#     if (i and i+1) in list1:
#         len_con += 1
# print(len_con)

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i >= j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("enter a no"))
# n1 = 1
# n2 = 1
# for i in range(1, n+1):
#     for j in range(1, (n*2)-1):
#         if j >= n1 and j <= n2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     n2 += 1

# n = int(input("enter a no"))
# n1 = n
# n2 = n
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j >= n1 and j <= n2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     n1 -= 1

# n = int(input("enter a no"))
# n1 = 1
# n2 = n
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j >= n1 and j <= n2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     n1 += 1


# n = int(input("enter a no"))
# n1 = 1
# n2 = n
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j >= n1 and j <= n2:
#             print("  *", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     n1 += 1


# n = int(input("enter a no"))
# n1 = 1
# n2 = n
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j >= n1 and j <= n2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     n2 -= 1

# while True:
#     n = int(input("enter a no"))
#     n1 = 1
#     n2 = n*2-1
#     for i in range(1, n+1):
#         for j in range(1, n2+1):
#             if j >= n1 and j <= n2:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
#         n1 += 1
#         n2 -= 1

# while True:
#     n = int(input("enter a no"))
#     n1 = n
#     n2 = n
#     for i in range(1, n+1):
#         for j in range(1, (n2*2)):
#             if j >= n1 and j <= n2:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
#         n1 -= 1
#         n2 += 1

'binary search'
# data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target = 13
# n1 = 0
# n2 = len(data)-1
# while n1 <= n2:
#     mid = (n1+n2)//2
#     if data[mid] == target:
#         print("found")
#         break
#     elif target > data[mid]:
#         n1 = mid+1
#     elif target < data[mid]:
#         n2 = mid-1

'linear search'
# data = [4, 2, 7, 1, 9, 5, 3, 8, 6, 10]
# target = 8
# result = False
# index = 0
# for i in data:
#     if target == i:
#         result = True
#         index = data.index(i)
# if result:
#     print("found", index)

'bubble sort'
# data = [5, 2, 9, 1, 7, 4, 8, 3, 6, 10]
# for i in range(0, len(data)):
#     for j in range(0, len(data)-1-i):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j+1], data[j]
# print(data)
