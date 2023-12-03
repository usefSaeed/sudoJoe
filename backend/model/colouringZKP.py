from backend.backendGlobal import writeJSON,get_proof_path


class ColouringZKP:
    def __init__(self,commitments,revealedCells):
        self.__commitments = commitments
        self.__revealedCells = revealedCells

    def serialize(self,gameIndex,fiatShaIndex):
        zk = {
            "commitments": self.__commitments,
            "revealed": self.__revealedCells
        }
        writeJSON(get_proof_path(gameIndex,fiatShaIndex),zk)




