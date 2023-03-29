from random import choice as r

def get_range(lst, min, max):
    return [x for x in lst if min <= x <= max]

def get_random_item(lst):
    return r(lst)

def second_min(lst):
    first_min = lst[0]
    second_min = lst[0]
    for num in lst:
        if num < first_min:
            second_min = first_min
            first_min = num

        elif num < second_min:
            second_min = num

    return second_min