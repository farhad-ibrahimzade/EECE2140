
def get_paths(m, n) -> list:
    """This function gets all possible paths with coordinates from (0,0) to the specified location

    Args:
        m (int): rows index
        n (int): columns index

    Returns:
        list: list of all possible paths
    """
    if m == 1:
        return [[(0,k) for k in range(n)]]
    
    if n == 1:
        return [[(k,0) for k in range(m)]]
    
    right = get_paths(m, n-1)  # Get all the paths without the rightmost column

    down = get_paths(m-1, n)  # Get all the paths without the bottom row

    corner = (m-1,n-1)  # Botton right corner
    
    right_paths = [rights + [corner] for rights in right]  # Add the corner to all paths

    down_paths = [downs + [corner] for downs in down]  # Add the corner to all paths 

    output = right_paths + down_paths

    return output

print(get_paths(4,4))