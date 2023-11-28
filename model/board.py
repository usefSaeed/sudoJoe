from model.cell import Cell
from globalData import *


class Board:

    def __init__(self, game):
        self.__grid = [[Cell() for _ in range(GAME_SIDE_LENGTH + 1)] for _ in range(GAME_SIDE_LENGTH + 1)]
        for r in range(GAME_SIDE_LENGTH):
            for c in range(GAME_SIDE_LENGTH):
                current_value = game[r][c]
                if current_value != 0:
                    self.__grid[r + 1][c + 1].set(current_value)

    def permute(self, p):
        for r in range(1, 1 + GAME_SIDE_LENGTH):
            for c in range(1, 1 + GAME_SIDE_LENGTH):
                self.__grid[r][c].set(p[int(self.__grid[r][c])])

    def show(self):
        for r in range(1, 1 + GAME_SIDE_LENGTH):
            for c in range(1, 1 + GAME_SIDE_LENGTH):
                print(self.__grid[r][c] if not self.__grid[r][c].is_empty() else "_", end=" ")
            print()
