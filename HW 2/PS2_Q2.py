'''The program checks if the user-entered matrix is a magic square'''

matrix = []
magic = True
i = 0

print("--------------------------------------------------------------")

# The loops allows to obtain a matrix of any size from the user
while True:
    print("Row", i + 1)
    row = input("Input the next row or press Enter to end: ")
    if row == "":
        break
    numbers = [int(x) for x in row.split()]
    matrix.append(numbers)

    i += 1

rows = len(matrix)
columns = len(matrix[0])

# Check if the matrix is square
if rows != columns:
    print("The matrix is not a magic square")

else:
    sums = []

    # Calculate the sums of rows
    for i in range(0, rows):
        sums.append(sum(matrix[i]))
        if max(matrix[i]) > rows*columns or min(matrix[i]) < 1:
            # Check for illegal values in the matrix
            magic = False

    # Calculate the sums of columns
    for i in range(0, columns):
        numSum = 0
        for j in range(0, rows):
            numSum += matrix[j][i]

        sums.append(numSum)

    # Calculate diagonal sums
    leftDiagonal = 0
    rightDiagonal = 0
    for i in range(0, columns):
        leftDiagonal += matrix[i][i]

    for i in range(0, rows):
        rightDiagonal += matrix[i][columns-1-i]

    sums.extend([leftDiagonal, rightDiagonal])

    if len(set(sums)) != 1:
        magic = False

    if magic:
        print("The matrix is a magic square")

    else:
        print("The matrix is not a magic square")
