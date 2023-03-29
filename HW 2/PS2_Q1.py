'''The program prints all prime numbers before the user entered integer'''

import math

print("--------------------------------------------------------------")

num = int(input("Please input your number: "))

integers = [nums for nums in range(2, num + 1)]

# Get the list of prime numbers using Sieve of Erathostenes method
for i in range(0, len(integers)):
    if integers[i] != 0:
        for j in range(i + integers[i], len(integers), integers[i]):
            integers[j] = 0

primes = [prime for prime in integers if prime != 0]

print(primes)
