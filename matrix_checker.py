import numpy as np

a = np.arange(1,10).reshape(3,3)

def row_contain(a, n):
    return np.count_nonzero(np.any(a == n, axis=1))

print(a)

print(row_contain(a, 3))