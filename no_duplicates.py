
lst = input("Enter the list of numbers: ").split()

s = set(lst)

newList = list(s)

newList.sort()

for num in newList:
    print(num, end=" ")