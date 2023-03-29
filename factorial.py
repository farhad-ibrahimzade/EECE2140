
def get_factorial(num):
    if num >= 0:
        factorial = 1
        for i in range(2,num + 1):
            factorial*=i
        return factorial
    else:
        raise Exception("Cannot compute factorial of a negative number")

number = int(input("Enter the number: "))
print("The factorial of", number, "is", get_factorial(number))