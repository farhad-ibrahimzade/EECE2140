'''The program sorts 3 numbers in increasing order'''

a = float(input("Please input the first number: "))
b = float(input("Please input the second number: "))
c = float(input("Please input the third number: "))

print("--------------------------------------------------------------")

# Numbers are compared to be sorted
if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b


print("Sorted numbers: %f, %f, %f" % (a, b, c))
