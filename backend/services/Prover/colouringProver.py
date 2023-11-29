from backend.model.board import Board
from backend.services.Prover.zkProverService import ZKProverService
from backend.globalData import permute


class ColouringProver(ZKProverService):
    def __init__(self, gameIndex):
        super().__init__(gameIndex)
        self.__P = [None]

    def __generate_permutation(self):
        nums = [i for i in range(1,10)]
        permute(nums)
        self.__P += nums

    def prove(self):
        self.__generate_permutation()
        self._solution.show()
        permuted_solution: Board = self._solution
        permuted_solution.permute(self.__P)




cpzk = ColouringProver(1)
cpzk.prove()
