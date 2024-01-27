from frontend.model.boards.colouringBoard import ColouringBoard
from frontend.services.zkVerifierService import ZKVerifierService
from frontend.frontendGlobal import GAME_SIDE_LENGTH, ROW, COL, SUBGRID, TYPE_COUNT, readJSON, get_proof_path, \
    delete_file, get_proof_title,PROOFS_TEMP_DIRECTORY


class ColouringVerifier(ZKVerifierService):
    CHALLENGE_RANGE = GAME_SIDE_LENGTH * TYPE_COUNT + 1

    def __init__(self, gameIndex,proofsCount):
        super().__init__(gameIndex)
        self.__gameIndex = gameIndex
        self.__colouringVerifier = None
        self.__proofsCount = proofsCount

    def verify(self):
        for proofIdx in range(self.__proofsCount):
            currentProofPath = get_proof_path(self.__gameIndex,proofIdx)
            proofData = readJSON(currentProofPath)
            self.__colouringVerifier = ColouringBoard(proofData['commitments'], proofData['revealed'])
            self.__colouringVerifier.clone_board(self._game)
            self.__colouringVerifier.place_commitments()
            challenge = self.__colouringVerifier.compute_challenge()
            if not self.__is_bullet_proof(challenge):
                print("########## PROOF INVALID ##########")
                print(self.__colouringVerifier.get_proof_bust())
                delete_all_files(PROOFS_TEMP_DIRECTORY)
                return False
            print("Verified",get_proof_title(self.__gameIndex,proofIdx))
            delete_file(currentProofPath)
        print("Probability that prover is cheating:",round(100*(((self.CHALLENGE_RANGE-1)/self.CHALLENGE_RANGE)**self.__proofsCount),2),"%")
        return True

    def __is_bullet_proof(self, challenge):
        match challenge:
            case n if n <  GAME_SIDE_LENGTH * (ROW + 1):
                return self.__colouringVerifier.verify_row(n - GAME_SIDE_LENGTH * ROW)
            case n if n <  GAME_SIDE_LENGTH * (COL + 1):
                return self.__colouringVerifier.verify_col(n - GAME_SIDE_LENGTH * COL)
            case n if n <  GAME_SIDE_LENGTH * (SUBGRID + 1):
                return self.__colouringVerifier.verify_subgrid(n - GAME_SIDE_LENGTH * SUBGRID)
            case n if n == GAME_SIDE_LENGTH * TYPE_COUNT:
                return self.__colouringVerifier.verify_filled_in_cells()



