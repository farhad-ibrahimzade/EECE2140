
import os
import sys


fractions = open(os.path.join(sys.path[0], "fractions.txt"))

fractDict = {}

min = float('inf')
min_str = None

max = - float('inf')
max_str = None

for line in fractions:
    nums = [int(char) for char in line.split("/")]
    string = line.replace("\n", "")
    value = nums[0] / nums[1]
    if value < min:
        min = value
        min_str = string

    if value > max:
        max = value
        max_str = string

print("Min:", min_str)
print("Max:", max_str)
