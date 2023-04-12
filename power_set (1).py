
def get_power_set(A: set):
    lst = list(A)
    if lst == []:
        return {}
    
    if len(lst) == 1:
        return A

    output = []
    output.extend(get_power_set(set(lst[:-1])))
    output.extend(elem + lst[-1] for elem in get_power_set(set(lst[:-1])))

    return set(output)

print(get_power_set({1,2,3}))
