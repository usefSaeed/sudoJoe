from model.board import Board
from services.Prover.zkProverService import ZKProverService
import random as r


class ColouringProver(ZKProverService):
    def __init__(self, gameIndex):
        super().__init__(gameIndex)
        self.__P = [None]

    def __generate_permutation(self):
        nums = [i for i in range(1,10)]
        r.shuffle(nums)
        self.__P += nums

    def prove(self):
        self.__generate_permutation()
        permuted_solution: Board = self._solution
        permuted_solution.permute(self.__P)


cpzk = ColouringProver(1)
cpzk.prove()
