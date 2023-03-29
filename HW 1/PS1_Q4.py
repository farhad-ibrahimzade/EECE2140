'''The program generates an equilateral triangle formed of * symbols
 with the amount of rows determined by user input'''

n = int(input("Enter a positive integer: "))

print("--------------------------------------------------------------")

# The value entered for the number of rows is checked for validity
if n < 1:
    print("Invalid input. Please enter a positive integer")

else:
    # The loop prints the appropriate amount of * symbols
    # and centers them using spaces to produce a triangle
    for i in range(0, n):
        print(" " * ((n - 1) - i) + ("*" * (i*2 + 1)))
