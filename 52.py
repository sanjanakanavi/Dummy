# coding exercise
'calculate the no of cans of paint needed'
import math
'1 can paint(coverage) = 7 sq meter'
'no of cans needed=(height*width)/7'
h = int(input("enter the height of wall in sq meters\n"))
w = int(input("enter the width of wall in sq meters\n"))
coverage = 7


def paint_calculator(height, width, cover):
    area = height*width
    no_of_cans = math.ceil(area/cover)
    print(f"you will need {no_of_cans} cans of paint")


paint_calculator(height=h, width=w, cover=coverage)
