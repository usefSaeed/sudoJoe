from frontend.model.colouringBoard import ColouringBoard
from frontend.services.zkVerifierService import ZKVerifierService
from frontend.frontendGlobal import GAME_SIDE_LENGTH,ROW,COL,SUBGRID,TYPE_COUNT,readJSON,get_proof_path


class ColouringVerifier(ZKVerifierService):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1

    def __init__(self, gameIndex,proofsCount):
        super().__init__(gameIndex)
        self.__gameIndex = gameIndex
        self.__colouringVerifier = None
        self.__proofsCount = proofsCount

    def verify(self):
        for proofIdx in range(self.__proofsCount):
            proofData = readJSON(get_proof_path(self.__gameIndex,proofIdx))
            self._colouring_prover = ColouringBoard(proofData['commitments'], proofData['revealed'])
            challenge = self.__colouringVerifier.compute_challenge()
            if not self.__challenge_handler(challenge):
                return False
        return True

    def __challenge_handler(self, challenge):
        match challenge:
            case n if n <  GAME_SIDE_LENGTH * (ROW + 1):
                return self._colouring_prover.verify_row(n - GAME_SIDE_LENGTH * ROW)
            case n if n <  GAME_SIDE_LENGTH * (COL + 1):
                return self._colouring_prover.verify_col(n - GAME_SIDE_LENGTH * COL)
            case n if n <  GAME_SIDE_LENGTH * (SUBGRID + 1):
                return self._colouring_prover.verify_subgrid(n - GAME_SIDE_LENGTH * SUBGRID)
            case n if n == GAME_SIDE_LENGTH * TYPE_COUNT:
                return self._colouring_prover.verify_filled_in_cells()

cpzk = ColouringVerifier(1,146)
cpzk.verify()
