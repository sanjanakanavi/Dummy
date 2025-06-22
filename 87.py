# method overloading and overriding
# method overloading: having multiple methods of same name with different parameters in a same class'

'lets take an example of typical metod overloading'

'''
class Addition:
    def add(a, b):  # add method with 2 parameters
        return a+b

    def add(a, b, c):  # another add method with 3 parameters
        return a+b+c


ad1 = Addition()  # object
print(ad1.add(1, 2))  # passign 2 parameters'''

'so here it will give error bcz add method with 3 parameters fails,so python doesnot support method overloading'

'there are 2 ways to achieve it '
'1: to make unnecssary parameter as default keeping its value 0'

'example for 1st way'

'''
class Addition:
    def add(self, a, b, c=0):  # method with 3 parameters but c is 0
        return a+b+c


ad1 = Addition()
# here u can pass 2 parameter or 3 parameter bcz when u pass 2 parameters c will be defined as 0
print(ad1.add(2, 2))
print(ad1.add(2, 2, 2))  # here c value will be overrided by value 2
'''

'2nd way is to accept infinity parameters in a method ,example'

'''
class demo:
    def add(self, *args):  # *args will accept infinity parameters
        total = 0
        for i in args:  # adding infinity nums
            total += i
        return total


d1 = demo()
print(d1.add(1, 2, 3, 4, 5, 6, 7, 8))  # can pass more parameters
'''

'method overriding :having same method name and same no of parameters in different classes that too inherited(parent and child class)'

'''
class Father:
    def sleep(self):
        print("sleep time from 9 pm to 6 am")

    def eat(self):
        print('eating')


class Son(Father):
    def sleep(self):  # this method having same name and no od parameters but diffrent content
        'according to mro priority check 1st it will consider its own sleep method and ignores father class method'
        'this overriding of data is called method overriding'
        print("sleeping time 2 am to 9 am")


s1 = Son()
s1.sleep()  # prints its own sleep method
'if we want to print parent method we can use: super().sleep()'
'''
