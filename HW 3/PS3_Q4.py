"""This program returns how many times we cna eat sushi
from the kaiten belt to alternate the dishes"""

n = 6

lst = [1, 2, 3, 3, 2, 1]

k = 2


def kaitenSushi(number, dishesList, skipDishes):
    """Function determines how many dishes were eaten
    from the kaiten belt based on the number of dishes that will arrive,
    the types of dishes and how many previous dishes to compare.

    Args:
        number (int): number of dishes that will arrive
        dishesList (list): list of types of dishes
        skipDishes (int): previous dishes to compare

    Returns:
        int: how many dishes were eaten
    """
    eaten = 0

    eat = True

    previous = []

    for dish in dishesList:

        if skipDishes <= len(previous):
            for i in range(skipDishes):
                if previous[i] == dish:
                    eat = False

        previous.append(dish)
        if eat:
            eaten += 1

    return eaten


print("Eaten:", kaitenSushi(n, lst, k))
