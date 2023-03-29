
def getNum(i):
    if i == 1:
        return int(input("Enter the first number: "))
    elif i == 2:
        return int(input("Enter the second number: "))

while True:
    try:
        x = getNum(1)
        y = getNum(2)
        print("Sum = ", x + y)
        break

    except ValueError:
        print("Invalid value entered")
   
