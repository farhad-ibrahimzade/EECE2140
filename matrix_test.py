import numpy as np

a = np.linspace(0,100,15).reshape(3,5)

# 3 students
# 5 exams

print(a)

print("average: ", a.mean(axis=1))

print("std deviation ", a.std(axis=0))

print("Lowest avg: ", np.argmin(a.mean(axis=0)))

print("Highest grade: ", np.argmax(a.max(axis=1)))

print("Highest avg", np.argmax(a.mean(axis=1)))

b = a.mean(axis=0)
print("Good avg: ", b[b > 60])
