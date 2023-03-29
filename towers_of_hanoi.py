
def hanoi(n, fr, to, spare):
    if n == 1:
        print_move(n, fr, to)

    else:
        hanoi(n - 1, fr, spare, to)
        print_move(n, fr, to)
        hanoi(n-1, spare, to, fr)

def print_move(disk, fr, to):
    print("Move disk ", disk, "from ", fr, "to ", to)

hanoi(3, "A", "B", "C")