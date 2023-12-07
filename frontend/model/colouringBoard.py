from frontend.model.verifierBoard import VerifierBoard
from frontend.frontendGlobal import GAME_SIDE_LENGTH, SUBGRID_SIDE_LENGTH, TYPE_COUNT, pseudo_random_num,xor_all_mod_n


class ColouringBoard(VerifierBoard):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1

    def __init__(self,commitments,revealedCells):
        super().__init__()
        self.__commitments = commitments
        self.__place_commitments()
        self.__revealedCells = revealedCells

    def __flatten_commitments(self):
        result = []
        for r in self.__commitments:
            for c in r:
                result.append(c)
        return result

    def __place_commitments(self):
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

    def __distinction_check(self, revealedValues):
        distinctValues = [0 for i in range(GAME_SIDE_LENGTH+[self.VALID_COORDINATES[0]])]
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
        i = 0
        revealedValues = []
        for c in self._grid[row_idx + self.VALID_COORDINATES[0]][self.VALID_COORDINATES[0]:]:
            v = c.verify_commitment(self.__revealedCells[i])
            if not v:
                return False
            revealedValues.append(v)
            i += 1
        return self.__distinction_check(revealedValues)

    def verify_col(self,col_idx):
        i = 0
        revealedValues = []
        for r in self._grid[self.VALID_COORDINATES[0]:]:
            c = r[col_idx + self.VALID_COORDINATES[0]]
            v = c.verify_commitment(self.__revealedCells[i])
            if not v:
                return False
            revealedValues.append(v)
            i += 1
        return self.__distinction_check(revealedValues)

    def verify_subgrid(self,subgrid_idx):
        i = 0
        revealedValues = []
        start_row = (subgrid_idx // SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        start_col = (subgrid_idx % SUBGRID_SIDE_LENGTH) * SUBGRID_SIDE_LENGTH + self.VALID_COORDINATES[0]
        for r in range(start_row,start_row+SUBGRID_SIDE_LENGTH):
            for c in range(start_col,start_col+SUBGRID_SIDE_LENGTH):
                c = self._grid[r][c]
                v = c.verify_commitment(self.__revealedCells[i])
                if not v:
                    return False
                revealedValues.append(v)
                i += 1
        return self.__distinction_check(revealedValues)


    def verify_filled_in_cells(self):
        filledInCells = self.__get_filled_in()
        assert filledInCells==self.__revealedCells
        permutationBreaker = [0 for i in range(GAME_SIDE_LENGTH+[self.VALID_COORDINATES[0]])]
        for i in range(len(filledInCells)):
            c = filledInCells[i]
            permutedValue = c.verify_commitment(self.__revealedCells[i])
            if not permutedValue:
                return False
            realValue = c.get_real_value()
            if permutationBreaker[realValue] == 0:
                permutationBreaker[realValue] = permutedValue
            else:
                if permutationBreaker[realValue] != permutedValue:
                    return False
        return True





