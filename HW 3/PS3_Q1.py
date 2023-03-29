""""This program prints all the perfect numbers before 10,000"""


def isPerfect(num):
    """This function checks whether a number is a perfect number.
    A perfect number is an integer that is equal
    to the sum of its proper divisors.

    Args:
        num (int): number to be checked

    Returns:
        bool: True if number is perfect, False if not
    """
    sum = 0
    for i in range(1, num):
        if not num % i:
            sum += i

    return num == sum


def perfectNumbers(n):
    """This function outputs a list of perfect numbers less than or equal to n

    Args:
        n (int): number

    Returns:
        list: List of perfect numbers less than or equal to n
    """
    return [i for i in range(1, n+1) if isPerfect(i)]


print("Perfect numbers less than or equal to 10,000:")

for number in perfectNumbers(10000):
    print(number)
