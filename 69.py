class Instructor:  # creation of class
    def __init__(self):
        print("creating a new object")


'init function is used to initialize objects and its attributes'
'init function is called everytime whenever object is created'


instructor_1 = Instructor()  # creating an object/instance of class instructor
# this is a creation of attribute in object instructor_1
instructor_1.name = "sanjana"
instructor_1.address = "dharwad"
print(type(instructor_1))
print(instructor_1.name)  # printing attribute of an object
instructor_2 = Instructor()  # second object created for instructor class
instructor_2.name = "kartik"
print(instructor_2.name)


class Baby:
    diapers = 5  # class object variable

    def __init__(self, babyname, babyaddress):  # passing 2 parameters with any name
        self.name = babyname  # creating variables/attributes self.variablename = parameter name
        self.address = babyaddress
        # setting default value for an attribute,now every object created has default 0 followers
        self.followers = 0


# creating an object and passing parameters in it
baby1 = Baby("sanjana", "dharwad")
# printing created attributes in init function
print(baby1.name, baby1.address, baby1.followers, baby1.diapers)
