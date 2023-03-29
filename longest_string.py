
strings = []

i = 0

while True:
    print("Point", i + 1)
    row = input("Input the next point or press Enter to end: ")
    if row == "":
        break
    string = [x for x in row.split()]

    strings.append(string)

    i += 1

longestString = max(strings, key = len)

print(longestString)