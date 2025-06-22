# Random module
'random module is builtin module which has functions which help in choosing random objects or data'
import random
# a<=x<=b means starting and ending points are included,here it randomly chooses between 1 to 3
a = random.randint(1, 3)
print(a)
# here in randrange funtion ending point is not included i,e a<=x<b, 3 is not included
b = random.randrange(1, 3)
print(b)
c = random.random()  # random fuction returns floating point number between 0.0 to 1.0 ,where ending point 1.0 is not included
print(c)
# uniform returns floating point number,ending point is not included,we can specify the range of numbers
d = random.uniform(1, 3)
print(d)
l = [10, 20, 30, 40, 50, 60]
e = random.choice(l)  # it will choose one of the sequence
print(e)
random.shuffle(l)  # shuffling the list
print(l)
