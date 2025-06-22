# now we see how to add methods to class
class Instructor:  # creating a class
    followers = 0  # default attribute

    def __init__(self, name, address):  # init function to initialize objects/attributes
        self.name = name  # attributes
        self.address = address

    def display(self, subject_name):  # creating a function in class i.e method,self is compulsary
        # using attributes to other functions like self.name
        # we can use parameters directly without using self. in methods of its parameters but not from attributes
        print(f"hello baby, its me {self.name} and i teach {subject_name}")

    # creating a function to update followers,it will accept follower name
    def update_folllowers(self, follower_name):
        'instead of self.followers we can specify it as Instructor.followers ,both are same'
        self.followers += 1  # whenever it accepts followername followers will be increased by 1


# creating an object and passing parameters
instructor_1 = Instructor("sanjana", "kanavi")
print(instructor_1.name, instructor_1.address)  # printing attributes of object
instructor_1.display("python")  # calling display function using object
# calling a function and passing a follower name
instructor_1.update_folllowers("kartik")
