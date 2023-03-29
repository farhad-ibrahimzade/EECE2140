
A = [[1,2],
    [4,3]]

B = [[4,3],
    [1,2]]

product = []

result = []

for i in range(0,len(A)):
    for j in range (0,len(A[i])):
        product.append(A[i][j] * B[j][i])
        
    result.append(product)

print(result)