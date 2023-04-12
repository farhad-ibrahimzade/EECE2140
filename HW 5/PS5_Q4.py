
def partition(a: list, p: int, r: int) -> int:
    """This function partitions a list for quicksort sorting and returns
    an index to use for further partition

    Args:
        a (list): list to partition
        p (_type_): lower index bound
        r (_type_): upper parttion bound

    Returns:
        int: index for further partition
    """
    x = a[r]  # Pivot
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        
    a[i + 1], a[r] = a[r], a[i+1]

    return i + 1

def quicksort(a: list, p: int ,r: int) -> list:
    """This function sorts a list using the quicksort method.

    Args:
        a (list): list to sort
        p (int): lower index bound
        r (int): upper index bound

    Returns:
        list: sorted list
    """
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q + 1, r)

    return a

print(quicksort([13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21], 0, 11))