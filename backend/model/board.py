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
                    self.__grid[R][C] = Cell(current_value, R, C)
                else:
                    self.__grid[R][C] = Cell()

    def __int__(self):
        result = 0
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                digitIdx = r*GAME_SIDE_LENGTH+c
                result += self.__grid[r][c] * 10**digitIdx
        return result

    def extract_solution(self,solution):
        extractedSolution = copy_object(self)
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                extractedSolution[r][c].set(solution[r-1][c-1])
        return extractedSolution


    def permute(self, p):
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                self.__grid[r][c].set(p[int(self.__grid[r][c])])

    def commit(self):
        committedSolution = [[None for _ in range(GAME_SIDE_LENGTH + 1)] for _ in range(GAME_SIDE_LENGTH + 1)]
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                committedSolution[r][c] = self.__grid[r][c].commit_cell()
        return committedSolution

    def reveal_row(self,row_idx):
        return [i.reveal_cell() for i in self.__grid[row_idx][self.VALID_COORDINATES[0]:]]

    def reveal_col(self,col_idx):
        return [r[col_idx].reveal_cell() for r in self.__grid[self.VALID_COORDINATES[0]:]]

    def reveal_subgrid(self,subgrid_idx):
        start_row = (subgrid_idx % SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        start_col = (subgrid_idx // SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        revealedSubgrid = [None for i in range(GAME_SIDE_LENGTH)]
        fillingIdx = 0
        for r in range(start_row,start_row+SUBGRID_SIDE_LENGTH):
            for c in range(start_col,start_col+SUBGRID_SIDE_LENGTH):
                revealedSubgrid[fillingIdx] = self.__grid[r][c].reveal_cell()
                fillingIdx += 1

    def reveal_filled_in_cells(self):
        filled_in_cells = []
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                current_cell = self.__grid[r][c]
                if current_cell.is_originally_filled_in():
                    filled_in_cells.append(current_cell.reveal_cell())

