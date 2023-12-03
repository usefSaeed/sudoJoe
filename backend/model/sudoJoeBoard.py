from backend.model.abstractBoard import AbstractBoard
from backend.model.cell import Cell
from backend.globalData import GAME_SIDE_LENGTH,SUBGRID_SIDE_LENGTH,copy_object


class Board(AbstractBoard):

    def __init__(self, game):
        super().__init__()
        for r in range(GAME_SIDE_LENGTH):
            for c in range(GAME_SIDE_LENGTH):
                current_value = game[r][c]
                R = r + 1
                C = c + 1
                if current_value != 0:
                    self._grid[R][C] = Cell(current_value)
                else:
                    self._grid[R][C] = Cell()

    def __int__(self):
        result = 1
        for r in self.VALID_COORDINATES[::-1]:
            for c in self.VALID_COORDINATES[::-1]:
                digitIdx = (GAME_SIDE_LENGTH-r)*GAME_SIDE_LENGTH+(GAME_SIDE_LENGTH-c)
                result += int(self._grid[r][c]) * 10**(digitIdx+1)
        result += 10**82
        return result



