from backend.model.colouringBoard import ColouringBoard
from backend.services.Prover.zkProverService import ZKProverService
from backend.backendGlobal import permute,GAME_SIDE_LENGTH,ROW,COL,SUBGRID,TYPE_COUNT,get_exponent


class ColouringProver(ZKProverService):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1

    def __init__(self, gameIndex):
        super().__init__(gameIndex)
        self.__gameIndex = gameIndex
        self._colouring_prover = None
        self.__P = [None]

    def __generate_permutation(self):
        nums = [i for i in range(1,10)]
        permute(nums)
        self.__P = [None]
        self.__P += nums

    def prove(self,fiatShaCount=1000,tolerable_perc=None):
        if tolerable_perc is not None:
            cheating_perc = (self.CHALLENGE_RANGE-1)/self.CHALLENGE_RANGE
            fiatShaCount = get_exponent(tolerable_perc,cheating_perc)
        self._game.show()
        for fiatShaIdx in range(fiatShaCount):
            self.__generate_permutation()
            self._colouring_prover = ColouringBoard(self._solution, self.__P)
            print(self.__P)
            self._colouring_prover.show()
            self._colouring_prover.commit()
            challenge = self._colouring_prover.create_challenge()
            self.__challenge_handler(challenge)
            zkProof = self._colouring_prover.construct_proof()
            zkProof.serialize(self.__gameIndex,fiatShaIdx)

    def __challenge_handler(self, challenge):
        match challenge:
            case n if n <  GAME_SIDE_LENGTH * (ROW + 1):
                self._colouring_prover.reveal_row(n - GAME_SIDE_LENGTH * ROW)
            case n if n <  GAME_SIDE_LENGTH * (COL + 1):
                self._colouring_prover.reveal_col(n - GAME_SIDE_LENGTH * COL)
            case n if n <  GAME_SIDE_LENGTH * (SUBGRID + 1):
                self._colouring_prover.reveal_subgrid(n - GAME_SIDE_LENGTH * SUBGRID)
            case n if n == GAME_SIDE_LENGTH * TYPE_COUNT:
                self._colouring_prover.reveal_filled_in_cells()

cpzk = ColouringProver(1)
cpzk.prove(tolerable_perc=0.005)
