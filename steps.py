
def climb_strairs(n):
    if n == 1 or n == 2:
        return n
    
    return climb_strairs(n-1) + climb_strairs(n-2)

#print(climb_strairs(4))

def display_ways(n):
    if n == 1:
        return [[1]]
    
    if n == 2:
        return [[1,1], [2]]
    
    # lst = []
    # lst1 = display_ways(n - 1)

    # for way in lst1:
    #     lst.append(way + [1])

    # lst2 = display_ways(n - 2)

    # for way in lst2:
    #     lst.append(way + [2])

    lst = [way + [1] for way in display_ways(n - 1)]
    lst += [way + [2] for way in display_ways(n - 2)]

    return lst

print(display_ways(4))


    