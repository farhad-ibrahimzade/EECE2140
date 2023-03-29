'''The program calculates the area of a triangle
based on the lengths of its sides using Heron's formula'''

import math

a = float(input("Please input the length of the first side: "))
b = float(input("Please input the length of the second side: "))
c = float(input("Please input the length of the third side: "))

print("--------------------------------------------------------------")

# The values entered for the sides are checked for validity
if a <= 0 or b <= 0 or c <= 0:
    print("The length of one of the sides is invalid")

else:
    s = (a + b + c) / 2  # s is the half perimeter of the triangle
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # The output is formatted to have 3 decimals
    print("The area of the triangle is: %.3f" % area)
