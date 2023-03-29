
def print_stars(num_stars):
    """Function prints a line of stars

    Args:
        num_stars (int): number of stars to print
    """
    for i in range(num_stars):
        print("*", end="")
    print()

print_stars(10)
print_stars(5)
print_stars