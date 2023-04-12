
def get_permutations(string: str) -> list:
    if len(string) == 2:
        return [string, string[::-1]]
    
    result = []
    for char in string:
        result.extend([txt + char for txt in get_permutations(string.replace(char, ""))])

    return result

print(get_permutations("abc"))


    

    

