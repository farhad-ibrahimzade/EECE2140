import numpy as np

a = np.arange(1,13).reshape(4,3)

# print(a[[2]])

# print(a[:, [1]])

# print(a[1:, 1:])

# print(a[[0,2], :])

# print(a[2:, 0:2])

print(a[1::2, ::2])