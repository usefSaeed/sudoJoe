from frontend.model.proofBusts.colouringCorrectnessBust import ColouringCorrectnessBust
from frontend.model.proofBusts.commitmentBust import CommitmentBust
from frontend.model.boards.verifierBoard import VerifierBoard
from frontend.frontendGlobal import GAME_SIDE_LENGTH, SUBGRID_SIDE_LENGTH, TYPE_COUNT, pseudo_random_num,xor_all_mod_n


class ColouringBoard(VerifierBoard):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1
    ROW = 0
    COL = 1
    SUBGRID = 2
    FILLED_IN = 3

    def __init__(self,commitments,revealedCells):
        super().__init__()
        self.__commitments = commitments
        self.__revealedCells = revealedCells
        self.__proofBust = None

    def __flatten_commitments(self):
        result = []
        for r in self.__commitments:
            for c in r:
                result.append(c)
        return result

    def place_commitments(self):
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                self._grid[r][c].save_commitment(self.__commitments[r-1][c-1])

    def __get_filled_in(self):
        filledInCells = []
        for r in self.VALID_COORDINATES:
            for c in self.VALID_COORDINATES:
                c = self._grid[r][c]
                if c.is_filled_in():
                    filledInCells.append(c)
        return filledInCells

    def __is_distinct(self, revealedValues):
        distinctValues = [0 for i in range(GAME_SIDE_LENGTH+1)]
        for v in revealedValues:
            distinctValues[v] += 1
        for i in self.VALID_COORDINATES:
            if distinctValues[i] != 1:
                return False
        return True

    def compute_challenge(self):
        seed = xor_all_mod_n(self.__flatten_commitments(),2**32)
        rd = pseudo_random_num(seed)
        return rd.randint(self.CHALLENGE_RANGE)

    def verify_row(self,row_idx):
        revealedValues = []
        for i in range(1,1+GAME_SIDE_LENGTH):
            c = self._grid[row_idx + 1][i]
            valueNoncePair = self.__revealedCells[i-1]
            v = c.verify_commitment(valueNoncePair)
            if not v:
                self.__proofBust = CommitmentBust(row_idx,i,valueNoncePair,c.get_commitment())
                return False
            revealedValues.append(v)
        if not self.__is_distinct(revealedValues):
            self.__proofBust = ColouringCorrectnessBust(self.ROW,row_idx+1)
            return False
        return True

    def verify_col(self,col_idx):
        revealedValues = []
        for i in range(1,1+GAME_SIDE_LENGTH):
            c = self._grid[i][col_idx + 1]
            valueNoncePair = self.__revealedCells[i-1]
            v = c.verify_commitment(valueNoncePair)
            if not v:
                self.__proofBust = CommitmentBust(i, col_idx, valueNoncePair, c.get_commitment())
                return False
            revealedValues.append(v)
        if not self.__is_distinct(revealedValues):
            self.__proofBust = ColouringCorrectnessBust(self.COL,col_idx+1)
            return False
        return True

    def verify_subgrid(self,subgrid_idx):
        i = 0
        revealedValues = []
        start_row = (subgrid_idx // SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + 1
        start_col = (subgrid_idx % SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + 1
        for r in range(start_row,start_row+SUBGRID_SIDE_LENGTH):
            for c in range(start_col,start_col+SUBGRID_SIDE_LENGTH):
                c = self._grid[r][c]
                valueNoncePair = self.__revealedCells[i]
                v = c.verify_commitment(valueNoncePair)
                if not v:
                    self.__proofBust = CommitmentBust(r, c, valueNoncePair, c.get_commitment())
                    return False
                revealedValues.append(v)
                i += 1
        if not self.__is_distinct(revealedValues):
            self.__proofBust = ColouringCorrectnessBust(self.SUBGRID,subgrid_idx+1)
            return False
        return True

    def verify_filled_in_cells(self):
        filledInCells = self.__get_filled_in()
        assert len(filledInCells)==len(self.__revealedCells)
        permutationBreaker = [0 for i in range(GAME_SIDE_LENGTH+1)]
        for i in range(len(filledInCells)):
            c = filledInCells[i]
            valueNoncePair = self.__revealedCells[i]
            permutedValue = c.verify_commitment(valueNoncePair)
            if not permutedValue:
                self.__proofBust = CommitmentBust(c.get_row(), c.get_col(), valueNoncePair, c.get_commitment())
                return False
            realValue = c.get_real_value()
            if permutationBreaker[realValue] == 0:
                permutationBreaker[realValue] = permutedValue
            else:
                if permutationBreaker[realValue] != permutedValue:
                    self.__proofBust = ColouringCorrectnessBust(self.FILLED_IN)
                    return False
        return True

    def get_proof_bust(self):
        return self.__proofBust





