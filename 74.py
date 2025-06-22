# multilevel inheritance in python
'generation line:grandparent,parent,child'


class Human:  # parent class 1
    can_breath = True

    def __init__(self, num_heart):
        print("calling init from human")
        self.eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("i can eat")

    def work(self):
        print("i can work")


class Male(Human):  # parent class 2,child of 1
    def __init__(self, name):
        self.name = name
        print("calling init from male")

    def sleep(self):
        print("i can sleep all day")


class Boy(Male):  # child class
    def __init__(self, can_dance, num_heart, name):
        self.can_dance = can_dance
        print("calling init from boy")
        Male.__init__(self, name)
        Human.__init__(self, num_heart)

    def work(self):
        super().work()  # using super inheriting grandparent method
        print("i can code")


boy_1 = Boy("yes", 1, "sanju")  # passing value of parameter for human class
boy_1.work()
print(boy_1.eyes)  # accessing attribute from grandparent class
print(Boy.mro())
print(boy_1.can_dance)
print(boy_1.can_breath)
