from backend.model.board import Board
from backend.model.colouringSJZK import ColouringSJZK
from backend.services.Prover.zkProverService import ZKProverService
from backend.globalData import permute,salty_sha256_mod,GAME_SIDE_LENGTH,ROW,COLUMN,SUBGRID


class ColouringProver(ZKProverService):
    verifying_options_count = 28

    def __init__(self, gameIndex):
        super().__init__(gameIndex)
        self._permuted_solution = None
        self.__P = [None]

    def __generate_permutation(self):
        nums = [i for i in range(1,10)]
        permute(nums)
        self.__P += nums

    def prove(self,fiatShaCount):
        for fiatShaIdx in fiatShaCount:
            gameInt = int(self._game)
            self.__generate_permutation()
            self._permuted_solution: Board = self._solution
            self._permuted_solution.permute(self.__P)
            committedSolution = self._permuted_solution.commit()
            proof_indicator = salty_sha256_mod(gameInt, fiatShaIdx, self.verifying_options_count)
            revealedCells = self.__proof_handler(proof_indicator)

    def __proof_handler(self, proof_num):
        match proof_num:
            case n if n <  GAME_SIDE_LENGTH:
                return self._permuted_solution.reveal(ROW, n)
            case n if n <  GAME_SIDE_LENGTH * 2:
                return self._permuted_solution.reveal(COLUMN, n)
            case n if n <  GAME_SIDE_LENGTH * 3:
                return self._permuted_solution.reveal(SUBGRID, n)
            case n if n == GAME_SIDE_LENGTH * 3:
                return self._permuted_solution.reveal_filled_in_Cells()





cpzk = ColouringProver(1)
cpzk.prove()
