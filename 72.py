# inheritance in python
'It is an ability to inherit features attributes methods from parent class to child class'
'inheritance enhance the reusability of the code'
# there will already created parent class as usual and when we create a child class
# its syntax is - Class childclassname(parentclassname):


class Human:  # parent class/normal class
    def __init__(self, num_heart):  # passing a parameter in parent class
        self.num_eyes = 2  # attributes
        self.num_nose = 1
        self.num_heart = num_heart  # creatign attribute for parameter

    def eat(self):  # method 1
        print("i can eat")

    def work(self):  # method 2
        print("i can work")


class Male(Human):  # child class inheriting properties from paremt class
    # parameter to accept name,we have to pass parameter heart here also of parent class parameter
    def __init__(self, name, heart):
        # inheriting parent init function atttributes,we have to pass parameter heart here also of parent class parameter
        super().__init__(heart)
        self.name = name  # attribute name

    def flirt(self):  # method of child class
        print("i can flirt")

    def work(self):  # reimplimenting parent method
        super().work()  # with the use of super keyword we can inherit all attributes and methods from same method of parent class
        'it will print both parent and child class content of method work'
        print("i can code")

    def display(self):
        # here we can access num_heart without super bcz methods are not same
        print(f"hi im {self.name} and i have {self.num_heart} heart")


# object of child class,we have to pass value for parent parameter num_heart here when we create objects
male_1 = Male("ram", 1)
male_1.eat()  # can access both its own methods and parents methods
male_1.work()
male_1.flirt()
# accessing attributes from parent class
print(male_1.num_nose, male_1.num_eyes)
print(male_1.name, male_1.num_heart)
male_1.display()  # calling display function
