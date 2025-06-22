# multiple inheritance in python
'in multiple inheritance multiple parents are present and 1 child class'
"""assume there are 2 parent class,both having same method,then when u call the method through child class
method of first parent will be executed, if the same method also present in child class then child class
method will override the parent classes methods"""


class Human:  # parent 1
    def __init__(self, num_heart):  # attributes
        print("calling init from human")
        self.num_heart = num_heart
        self.eyes = 2
        self.nose = 1

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


class Male:  # parent 2
    def __init__(self, name):  # creating attributes from parameters
        print("calling init from male")
        self.name = name

    def flirt(self):
        print("i can flirt")

    def work(self):
        print("i can code")


class Boy(Human, Male):  # child class inheriting both parent class
    """when more then 2 parent class then first parent class init will be executed if we want specific init class then in child class 
    have to create init function and then we can call specific parent class init function
    its syntax is : parentclassname.__init__(parameters of parent class)"""

    def __init__(self, name, heart, language):
        # calling specific parent class init function in child class init function
        Male.__init__(self, name)
        Human.__init__(self, heart)
        self.language = language

    def sleep(self):
        print("i can sleep")

    def work(self):
        print("i can test")

    def display(self):
        print(f"hi im {self.name} and i work on {self.language} language")


boy_1 = Boy("kartik", 1, "python")  # creating object of child class
boy_1.work()  # calling method
"""here if we want to execute specific method from any class/parent class when multiple classes have same method
then the syntax is : classname.methodname(objectname)"""
Male.work(boy_1)
print(Boy.mro())  # method to find order of priority of Boy class
boy_1.display()
