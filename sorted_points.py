import math


points = []

i = 0

while True:
    print("Point", i + 1)
    row = input("Input the next point or press Enter to end: ")
    if row == "":
        break
    numbers = tuple([int(x) for x in row.split()])
    points.append(numbers)

    i += 1

def distance(obj):
    x = obj[0]
    y = obj[1]
    return math.sqrt(x**2 + y** 2)


sortedPoints = sorted(points, key=lambda p: p[0]**2 + p[1]**2)

print(sortedPoints)
