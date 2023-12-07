from frontend.model.abstractBoard import AbstractBoard
from frontend.model.verifierCell import VerifierCell
from frontend.frontendGlobal import GAME_SIDE_LENGTH,copy_object


class VerifierBoard(AbstractBoard):

    def __init__(self):
        super().__init__()

    def fill_from_file(self,game):
        for r in range(GAME_SIDE_LENGTH):
            for c in range(GAME_SIDE_LENGTH):
                current_value = game[r][c]
                R = r + 1
                C = c + 1
                if current_value != 0:
                    self._grid[R][C] = VerifierCell(current_value)
                else:
                    self._grid[R][C] = VerifierCell()

    def clone_board(self,board):
        assert isinstance(board, VerifierBoard)
        self._grid = copy_object(board._grid)

    def __int__(self):
        result = 1
        digitRange = GAME_SIDE_LENGTH + 1
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                digitIdx = (GAME_SIDE_LENGTH-r)*GAME_SIDE_LENGTH+(GAME_SIDE_LENGTH-c)
                result += int(self._grid[r][c]) * digitRange**(digitIdx+1)
        result += digitRange**(GAME_SIDE_LENGTH**2 + 1)
        return result





