from backend.globalData import GAME_SIDE_LENGTH


class AbstractBoard:
    valid_coordinate = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self):
        self.__grid = [[None for _ in range(GAME_SIDE_LENGTH + 1)] for _ in range(GAME_SIDE_LENGTH + 1)]

    def get(self,r,c):
        if r in self.valid_coordinate and c in self.valid_coordinate:
            return self.__grid[r][c]
        else:
            raise ValueError("Invalid cell coordinates for SudokuCell")

    def show(self):
        for r in self.valid_coordinate:
            for c in self.valid_coordinate:
                print(self.__grid[r][c], end=" ")
            print()