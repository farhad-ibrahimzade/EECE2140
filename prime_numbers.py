import math
num = int(input("Please input your number: "))
upper = int(math.sqrt(num)) #only need to check factors until the square root of the number
if num <=1:
    print("The number inputted is invalid")
else:
    prime = True
    for i in range(2, upper + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")