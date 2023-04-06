
def generate_passwords(characters: str, length: int) -> list:
    """This function generates all possible passwords that can be generated 
    from the provided list of characters up to the specified length

    Args:
        characters (str): characters to generate passwords from
        length (int): length of the password

    Returns:
        list: list of all possible passwords
    """
    if length == 1:
        return list(characters)
    
    passwords = []

    prev_passwords = generate_passwords(characters, length-1)
    
    for password in prev_passwords:
        passwords.append(password)
        for letter in list(characters):
            passwords.append(password+letter)

    return passwords

print(generate_passwords("abc", 2))