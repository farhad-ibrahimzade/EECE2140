
lst = [int(n) for n in input("Enter the list of integers: ").split()]

num = int(input("Enter the number: "))

def get_integers(number, integerList):
    numberSet = set()
    for i in integerList:
        if (number - i) in numberSet:
            return number - i, i

        numberSet.add(i)
        

print("Output:", get_integers(num,lst))