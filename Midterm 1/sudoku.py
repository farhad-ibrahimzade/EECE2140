
board = [[6,3,9,5,7,4,1,8,2],
        [5,4,1,8,2,9,3,7,6],
        [7,8,2,6,1,3,9,5,4],
        [1,9,8,4,6,7,5,2,3],
        [3,6,5,9,8,2,4,1,7],
        [4,2,7,1,3,5,8,6,9],
        [9,5,6,7,4,8,2,3,1],
        [8,1,3,2,9,6,7,4,5],
        [2,7,4,3,5,1,6,9,8]]

digits = set(range(1,10))

valid = True

sub = 0

for i in range (0,9):

    if set(board[i]) != digits:
        valid = False
        break

    column = set(board[j][i] for j in range(9))

    if column != digits:
        valid = False
        break

for i in range(3):
    for j in range(3):
        start_row = i*3
        start_col = j*3
        
        subgrid = set(board[k][l] for k in range(start_row, start_row + 3)
                                for l in range(start_col, start_col + 3))

        if subgrid != digits:
            valid = False
            break

print(valid)

