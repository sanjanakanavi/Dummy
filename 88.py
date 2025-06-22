# magic/dunder methods ,this methods allows us to use inbuilt methods


class Author:
    def __init__(self, name, bookname, pages):
        self.name = name
        self.bookname = bookname
        self.pages = pages

    def __len__(self):  # this is called when u print len(object)
        return self.pages

    def __str__(self):  # dunder method of string
        return f"{self.bookname} by {self.name}"

    # this method is called automaticaly when object with parenthesis is called
    def __call__(self, *args, **kwds):
        print("hi")

    def __del__(self):  # when del method i used it will execute this method
        print("d object has been deleted")


d = Author("sanjana", "ramayan", 1000)
print(d)  # if object has its string version in method __str__
# then that is executed by default when u print only object
# and also init is executed by default when u create an object
print(len(d))  # when we call len method on object ,then __len__ is called
d()
del d  # method to delete object ,but if u defined its inbuilt method,it will execute that
print(d)  # if u try to print d after using del method on it ,it will show error bcz it will be deleted
'using dunder method is ntg but modifying inbuilt methods as we want and excute them just by using objects'
'there are more dunder methods to study can find in google '
