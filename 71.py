# coding exercise
'find an area and circumference of a circle usinf oops concept by creating classes and objects'


class Circle:  # creating class of name circle
    pi = 3.14  # default attriute with value

    def __init__(self, radius):  # init function to recieve radius
        self.radius = radius  # radius attribute
        # here we created area attribute and we calculatd area here itself using expression
        # we can skip self. for radius bcz we can use parameters inside its own function directly
        self.area = self.pi*(radius*radius)

    def get_circumference(self):  # function to calculate circumference
        return 2*self.pi*self.radius  # returning a value of answer


circle_1 = Circle(4)  # object 1 ,passing rasdius
# printing radius attribute
print(f"the radius of circle 1 is:{circle_1.area}")
# calling and printing get_circumference method
print(f"the circumference of circle 1 is {circle_1.get_circumference()}")
circle_2 = Circle(14)  # same for object 2
print(f"the radius of circle 2 is:{circle_2.area}")
print(f"the circumference of circle 2 is {circle_2.get_circumference()}")


class Rectangle:  # creating class for rectangle
    def __init__(self, length, width):  # accepting length and width from parameters
        # creating attribute and calculating area using parameters directly
        self.area = length*width


rectangle_1 = Rectangle(5, 5)  # creating object
print(f"area of rectangle 1 is :{rectangle_1.area}")  # printing attribute area
