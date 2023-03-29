'''The program returns a transpose of a matrix A'''

print("--------------------------------------------------------------")

A = [[1, 2], [3, 4], [5, 6]]

transpose = [[row[column] for row in A] for column in range(len(A[0]))]

print(transpose)
