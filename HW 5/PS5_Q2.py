
def to_binary(n: int) -> str:
    """This function converts a decimal number to binary.

    Args:
        n (int): number in decimal to convert

    Returns:
        str: converted number in binary
    """
    if n == 1:
        return 1
    
    return str(to_binary(n//2)) + str(n%2)

