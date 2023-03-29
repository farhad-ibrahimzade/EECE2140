from matrix import Matrix

a = Matrix([[1, 2],
            [3, 4],
            [5, 6]
            ])

b = Matrix([[1, 2],
            [3, 4],
            [5, 6]
            ])

c = Matrix([[-2, -1, 0],
            [5, -7, 6]
            ])

# Testing all the operations

print("Adding two matrices")
print(a+b)

print("Substracting two matrices")
print(a-b)

print("Multiplying two matrices")
print(a*c)

print("Checking if two matrices are equivalent")
print(a==b)

print("Output the amount of elements in a matrix")
print(len(a))

print("Output the matrix")
print(c)

print("Transpose a matrix")
print(a.transpose())

print("Check if object is matrix")
print(Matrix.is_matrix(a))

print("Sort the matrix reversed")
print(a.sort(True))

print("Save matrix to binary file")
c.save(input("Input file name: "))

print("Read matrix from file")
print(c.load(input("Input file name: ")))


