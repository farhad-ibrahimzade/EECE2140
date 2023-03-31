
def get_paths(m, n):
    if m == 1:
        return [(0,k) for k in range(n)]
    
    if n == 1:
        return [(k,0) for k in range(m)]
    
    right = get_paths(m, n-1)

    down = get_paths(m-1, n)

    corner = (m-1,n-1)
    
    right_paths = [right + [corner]]

    down_paths = [down + [corner]]

    output = right_paths + down_paths

    return output

print(get_paths(2,2))