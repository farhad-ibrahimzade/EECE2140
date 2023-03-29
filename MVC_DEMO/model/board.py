from model.player import Player

class Board:

    EMPTY_CELL = 0

    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]  # underscore indicated the parameter is not used, it is a convention

    def __getitem__(self, index):
        row, col = index
        return self.matrix[row][col]
    
    def __setitem__(self, index, value):
        row, col = index
        self.matrix[row][col] = value

    def check_winner(self):
        # Check the rows
        for i in range(self.size):
            row = set(self.matrix[i])
            if row == {Player.X}:
                return Player.X
            elif row == {Player.O}:
                return Player.O
            
        # Check the columns
        for j in range(self.size):
            col = set(self.matrix[i][j] for i in range(self.size))
            if col == {Player.X}:
                return Player.X
            elif col == {Player.O}:
                return Player.O
            

        # Check the diagonals
        
        left_diag = set(self.matrix[i][i] for i in range(self.size))

        if left_diag == {Player.X}:
            return Player.X
        elif left_diag == {Player.O}:
            return Player.O

        right_diag = set(self.matrix[self.size - i - 1][self.size - i - 1] for i in range(self.size))

        if right_diag == {Player.X}:
            return Player.X
        elif right_diag == {Player.O}:
            return Player.O
        
        return 0
    
    def is_full(self):
        return set(self.matrix[i][j] for i in range(self.size) for j in range(self.size)) == {Board.EMPTY_CELL}
           