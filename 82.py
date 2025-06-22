# access specifiers
'public,private,protected'
'public: attributes and methods of class can be used anywhere and by any one'
'protected: attributes and methods of class can be used by only it or its derived class/child class'
'private:  attributes and methods of class cannot be used by anyone or child class ,only used by itself'
'we can make atttributes and methods both private or protected'
'if we call private method in another method in same class ,then call that method outside the class then it will access private data'
'same we can access private attributes by putting them in another method and calling that method outside'


class Student:
    def __init__(self, name, rollno, age):
        self.name = name  # by default public instance variable
        self._rollno = rollno  # by single underscore ,this is protected instance variable
        self.__age = age  # private instance variable with double underscore

    def display(self):
        print(
            f"hi myself {self.name} im from student class,my roll no is {self._rollno}, age is {self.__age}")


class Branch(Student):
    pass


s1 = Student("rahul", 10, 30)
# print(s1.name)
s1.display()  # private variable can be accessed by calling funct containing that private data
# b1 = Branch("nisha", 22, 30)
# print(b1._rollno)  # child class accessing protected data of parent class
# print(b1.__age)  # u cannot use private variable with devired class object also ERROR
# using dir method by passing object,it shows which variables and methods are private
# print(dir(s1))
# that is called namemangling
print(s1._Student__age)  # way to print private attribute value
