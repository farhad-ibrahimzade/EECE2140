
def get_power_set(A):
    if len(A) == 0:
        return [[]]

    # subsets = get_power_set(A[1:])
    # lst = []
    # for subset in subsets:
    #     lst.append(subset)
    #     lst.append([A[0]] + subset)

    lst = get_power_set(A[1:])
    lst += [[A[0]] + subset for subset in lst]
    
    return lst

print(get_power_set([1,2,3]))
