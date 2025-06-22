# love calculator program
name1 = input("enter the first name ")
name2 = input("enter the second name ")
combine = name1+name2
combine = combine.lower()
t = combine.count('t')
r = combine.count('r')
u = combine.count('u')
e = combine.count('e')
true = str(t+r+u+e)
l = combine.count('l')
o = combine.count('o')
v = combine.count('v')
e = combine.count('e')
love = str(l+o+v+e)
percent = int(true+love)
if percent < 10 or percent > 90:
    print(f"your love score is {percent} and u guys are like coke and mentos")
elif percent >= 40 and percent <= 50:
    print(f"your love score is {percent} and u guys go good together")
else:
    print(f"your love score is {percent}")
