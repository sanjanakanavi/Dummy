# hierarchical inheritance in python
'in thid 1 parent and multiple children'


class Human:  # parent class
    def __init__(self, name, age):
        print("calling init from human")
        self.name = name
        self.age = age

    def showdetails(self):
        print(f"name : {self.name} , age : {self.age}")

    def eat(self):
        print("i can eat")


class Male(Human):  # child 1
    def __init__(self, name, age, location):
        print("calling init from male")
        Human.__init__(self, name, age)
        self.location = location

    def sleep(self):
        print("i can sleep all day")


class Female(Human):  # child 2
    def __init__(self, name, age, can_dance):
        print("calling init from female")
        super().__init__(name, age)
        self.can_dance = can_dance

    def showdetails_f(self):
        Human.showdetails(self)  # acceessing method from parent class
        print(f"can you dance? : {self.can_dance}")

    def work(self):
        print("i can work")


male_1 = Male("ram", 20, "dwd")  # object of male

female_1 = Female("jiya", 20, "yes")  # object of female
female_1.eat  # accessing method of parent
female_1.showdetails_f()
