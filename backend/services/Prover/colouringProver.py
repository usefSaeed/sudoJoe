from backend.model.colouringSJZK import ColouringSJZK
from backend.services.Prover.zkProverService import ZKProverService
from backend.globalData import permute,salty_sha256_mod,GAME_SIDE_LENGTH
import math


class ColouringProver(ZKProverService):
    verifying_options_count = 28

    def __init__(self, gameIndex):
        super().__init__(gameIndex)
        self._permuted_solution = None
        self.__P = [None]

    def __generate_permutation(self):
        nums = [i for i in range(1,10)]
        permute(nums)
        self.__P = [None]
        self.__P += nums

    def prove(self,fiatShaCount=1000,tolerable_perc=None):
        sudoJoeProofs = []
        self._game.show()
        gameInt = int(self._game)
        if tolerable_perc is not None:
            cheating_perc = (self.verifying_options_count-1)/self.verifying_options_count
            fiatShaCount = math.ceil(math.log(tolerable_perc,cheating_perc))
        for fiatShaIdx in range(fiatShaCount):
            self.__generate_permutation()
            self._permuted_solution = self._solution.extract_permutation(self.__P)
            print(self.__P)
            self._permuted_solution.show()
            committedSolution = self._permuted_solution.commit()
            proofIndicator = salty_sha256_mod(gameInt, fiatShaIdx, self.verifying_options_count)
            revealedCells = self.__proof_handler(proofIndicator)
            zkProof = ColouringSJZK(gameInt,fiatShaIdx,committedSolution,revealedCells)
            sudoJoeProofs.append(zkProof)
        return sudoJoeProofs

    def __proof_handler(self, proof_num):
        match proof_num:
            case n if n <  GAME_SIDE_LENGTH:
                return self._permuted_solution.reveal_row(n)
            case n if n <  GAME_SIDE_LENGTH * 2:
                return self._permuted_solution.reveal_col(n - GAME_SIDE_LENGTH)
            case n if n <  GAME_SIDE_LENGTH * 3:
                return self._permuted_solution.reveal_subgrid(n - GAME_SIDE_LENGTH*2)
            case n if n == GAME_SIDE_LENGTH * 3:
                return self._permuted_solution.reveal_filled_in_cells()

cpzk = ColouringProver(1)
cpzk.prove(tolerable_perc=0.05)
