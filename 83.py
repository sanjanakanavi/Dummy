# encapsulation in python
'wrapping the data and methods / code into one unit is called encapsulation'
'encapsulation is done by using public,protected and private techniques as we saw in 82.py file'
'first method to access private data was to put attributes and methods in public function and calling that function'
'second method to acess private data was to use name mangling :dir(objectname) method ,print(objectname._classname__privateAttributeName/methodname)'
'third method is to use getter and setter method, getter is used to retrive privatedata ,setter is used to modify privatedata'
'getter method: get_variablename() , settermethod: set_variablename(parameter),parameter to change the value of private attribute'


class Student:
    def __init__(self, name, rollno, age):
        self.name = name
        self._rollno = rollno  # protected one
        self.__age = age  # private one

    def get_age(self):  # this is getter method,this is how we write getter method
        return self.__age  # returning private attribute

    def set_age(self, age):  # age parameter to fetch new value of age from user
        if age > 35:
            print("inavlid input")
        else:
            self.__age = age  # assigning new value to private attribute


s1 = Student("rahul", 10, 30)
print(s1.get_age())  # printing private attribute using get method
s1.set_age(25)  # 25 is new value for private attribute age
print(s1.get_age())  # again get method to check the value

'using getter and setter method is good to perform encapsulation'
'note: encapsulation is mostly achieved in implimentation and abstraction is mostly achieved in designing'
