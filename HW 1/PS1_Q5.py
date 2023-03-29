'''The program displays an amount of Fibonacci numbers set by the user'''

n = int(input("Enter the amount of Fibonacci numbers to display: "))

print("--------------------------------------------------------------")

# The value entered for the amount of numbers is checked for validity
if n < 1:
    print("Invalid input. Please enter a positive integer")

else:
    if n == 1:  # The first number in the sequence is predetermined
        nums = [0]
    else:
        nums = [0, 1]  # The first two numbers in the series are predetermined

        for i in range(2, n):
            nums.append(nums[i-1] + nums[i-2])  # Additional numbers are added

    print("Fibonacci numbers: ")

    for j in range(0, len(nums)-1):
        print(nums[j], end=", ")

    print(nums[len(nums) - 1], end="")
