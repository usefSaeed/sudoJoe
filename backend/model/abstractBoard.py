from backend.globalData import GAME_SIDE_LENGTH


class AbstractBoard:
    VALID_COORDINATES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self._grid = [[None for _ in range(GAME_SIDE_LENGTH + 1)] for _ in range(GAME_SIDE_LENGTH + 1)]

    def get(self,r,c):
        if r in self.VALID_COORDINATES and c in self.VALID_COORDINATES:
            return self._grid[r][c]
        else:
            raise ValueError("Invalid cell coordinates for SudokuCell")

    def show(self):
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                print(self._grid[r][c], end=" ")
            print()