num = int(input("Please input the number: "))

sum = 0

while num > 0:
    sum += num % 10
    num//=10

print("The sum is", sum)