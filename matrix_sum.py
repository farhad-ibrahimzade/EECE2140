matrix = []

i = 0

while True:
    print("Row", i + 1)
    row = input("Input the next row or press Enter to end: ")
    if row == "":
        break
    numbers = [int(x) for x in row.split()]
    matrix.append(numbers)

    i += 1

print(matrix)


