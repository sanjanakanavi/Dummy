# coding execise
'fizzbuzz question, in a sereies of number '
'if no is divisible by 3 then replace it by fizz'
'if no is divisible by 5 then replace it by buzz'
'if no is divisible by both 3 and 5 then replace it by fizzbuzz'
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = 'fizzbuzz'
    elif i % 3 == 0:
        i = 'fizz'
    elif i % 5 == 0:
        i = 'buzz'
    print(i)
