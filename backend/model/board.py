from backend.model.abstractBoard import AbstractBoard
from backend.model.cell import Cell
from backend.globalData import GAME_SIDE_LENGTH


class Board(AbstractBoard):

    def __init__(self, game):
        super().__init__()
        for r in range(GAME_SIDE_LENGTH):
            for c in range(GAME_SIDE_LENGTH):
                current_value = game[r][c]
                R = r + 1
                C = c + 1
                if current_value != 0:
                    self.__grid[R][C] = Cell(current_value, R, C)
                else:
                    self.__grid[R][C] = Cell()

    def permute(self, p):
        for r in self.valid_coordinate:
            for c in self.valid_coordinate:
                self.__grid[r][c].set(p[int(self.__grid[r][c])])

