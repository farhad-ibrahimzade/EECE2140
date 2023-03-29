'''The program is a simple calculator that takes two numbers
 and an operator and performs the requested calculation'''

a = float(input("Please input the first number: "))
b = float(input("Please input the second number: "))

# Only addition, substraction, product and division are supported
operator = input("Please enter the operator: ")

print("--------------------------------------------------------------")

# The result of the calculation is recorded and outputed to the user
if operator == "+":
    output = a + b

elif operator == "-":
    output = a - b

elif operator == "*":
    output = a * b

elif operator == "/":
    output = a / b

else:
    output = "Invalid operator"

print(a, operator, b, "= %f" % output)
