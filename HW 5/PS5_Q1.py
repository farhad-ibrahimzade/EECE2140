
def is_palindrome(string: str) -> bool:
    """This function checks if a word is a palindrom, meaning if 
    it reads the same both forward and backward.

    Args:
        string (str): word to check

    Returns:
        bool: True if word is a palindrome, False if not
    """
    if len(string) == 0 or len(string) == 1:
        return True
    

    if string[0] == string[-1]:
        return True
    
    is_palindrome(string[1:-1])

    return False

print(is_palindrome("racecar"))
    
