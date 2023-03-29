
f = open("number_powers.txt", mode="r+")

for i in range(1, 1001):
    print(i**1,i**2,i**3,i**4, file=f)

for i in f:
    line = f.readline()
    lst = line.split()
    print(str(lst[2]))
