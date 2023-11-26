from model.cell import Cell
SIDE_LENGTH = 9

class Board:
    def __init__(self,game):
        self.grid = [[Cell() for _ in range(10)] for _ in range(10)]
        for r in game:
            for c in game[r]:
                current_value = game[r][c]
                if current_value != 0:
                    self.grid[r+1][c+1].set(current_value)

    def show(self):
        for r in range(1,1+SIDE_LENGTH):
            for c in range(1,1+SIDE_LENGTH):
                print(self.grid[r][c] if self.grid[r][c]!=None else "_",end=" ")
            print()


