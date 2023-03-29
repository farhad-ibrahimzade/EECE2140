lst = []

num = 0

while True:
    num = int(input("Enter a number (enter -1 to end): "))
    if num == -1:
        break
    lst.append(num)

print(lst)
avg = sum(lst)/(len(lst))
print(f"The average of the list is:{avg:.3f}")