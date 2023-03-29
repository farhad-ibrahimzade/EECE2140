""""This program validates credit/debit/bank card numbers
 using The Luhn Algorithm"""


def validCard(string):
    """This function validates a credit, debit or bank card number
    (in four groups, separated by space) using the Luhn Algorithm

    Args:
        string (str): String containing the card number

    Returns:
        bool: True if card number is valid, False if not
    """
    string = string.replace(" ", "")

    numbers = [int(digit) for digit in string]

    numbers.reverse()

    for i in range(len(numbers)):
        if i % 2:
            numbers[i] *= 2
            if numbers[i] >= 10:
                numbers[i] = numbers[i] // 10 + numbers[i] % 10

    return sum(numbers) % 10 == 0


print("Valid:", validCard("4799 2739 8713 6272"))
