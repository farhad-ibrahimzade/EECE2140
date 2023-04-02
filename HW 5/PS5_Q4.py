
def partition(a: list, p, r) -> int:
        
    x = a[r]
    i = p - 1
    for j in range(p, r - 1):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        
    a[i + 1], a[r] = a[r], a[i+1]

    return i + 1

def quicksort(a: list, p: int ,r: int) -> list:
    
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q + 1, r)

    return a

print(quicksort([3,2,6,7,4,9,1], 0 , 6))