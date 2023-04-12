
def generate_passwords(letters: str, length: int):
    if length == 1:
        return list(letters)
    
    passwords = []

    prev_passwords = generate_passwords(letters, length-1)
    
    for password in prev_passwords:
        passwords.append(password)
        for letter in list(letters):
            passwords.append(password+letter)

    return passwords

print(generate_passwords("abc", 2))