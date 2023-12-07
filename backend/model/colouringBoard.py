from backend.model.colouringZKP import ColouringZKP
from backend.model.proverBoard import ProverBoard
from backend.backendGlobal import GAME_SIDE_LENGTH, SUBGRID_SIDE_LENGTH, TYPE_COUNT, pseudo_random_num,xor_all_mod_n


class ColouringBoard(ProverBoard):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1

    def __init__(self,solution,P):
        super().__init__()
        self.clone_board(solution)
        self.__committedSolution = None
        self.__revealedCells = []
        self.__permute(P)

    def __permute(self, p):
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                self._grid[r][c].set(p[int(self._grid[r][c])])

    def __flatten_commitments(self):
        result = []
        for r in self.__committedSolution:
            for c in r:
                result.append(c)
        return result

    def commit(self):
        self.__committedSolution = [[None for _ in range(GAME_SIDE_LENGTH)] for _ in range(GAME_SIDE_LENGTH)]
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                self.__committedSolution[r-1][c-1] = self._grid[r][c].commit_cell()


    def create_challenge(self):
        assert self.__committedSolution is not None
        seed = xor_all_mod_n(self.__flatten_commitments(),2**32)
        rd = pseudo_random_num(seed)
        return rd.randint(self.CHALLENGE_RANGE)

    def reveal_row(self,row_idx):
        assert self.__committedSolution is not None
        self.__revealedCells = [i.reveal_cell()
                        for i in self._grid[row_idx + self.VALID_COORDINATES[0]][self.VALID_COORDINATES[0]:]]

    def reveal_col(self,col_idx):
        assert self.__committedSolution is not None
        self.__revealedCells = [r[col_idx + self.VALID_COORDINATES[0]].reveal_cell()
                        for r in self._grid[self.VALID_COORDINATES[0]:]]

    def reveal_subgrid(self,subgrid_idx):
        assert self.__committedSolution is not None
        start_row = (subgrid_idx // SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        start_col = (subgrid_idx % SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        self.__revealedCells = [None for i in range(GAME_SIDE_LENGTH)]
        fillingIdx = 0
        for r in range(start_row,start_row+SUBGRID_SIDE_LENGTH):
            for c in range(start_col,start_col+SUBGRID_SIDE_LENGTH):
                self.__revealedCells[fillingIdx] = self._grid[r][c].reveal_cell()
                fillingIdx += 1

    def reveal_filled_in_cells(self):
        assert self.__committedSolution is not None
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                current_cell = self._grid[r][c]
                if current_cell.is_originally_filled_in():
                    self.__revealedCells.append(current_cell.reveal_cell())

    def construct_proof(self):
        assert self.__committedSolution is not None
        assert len(self.__revealedCells) >= GAME_SIDE_LENGTH
        return ColouringZKP(self.__committedSolution,self.__revealedCells)

