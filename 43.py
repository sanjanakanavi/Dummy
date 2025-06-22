# range function
'syntax: range(start(index), stop(exclude the ending point), stepsize)'
'if stepsize is negative it will print nothing if stop number is positive'
'stepsize cannot be zero'
a = range(10, 20, 2)
print(a)
print(a[4])
for i in a:
    print(i)
b = range(10, 0, -1)  # printing reverse range
for i in b:
    print(i)
