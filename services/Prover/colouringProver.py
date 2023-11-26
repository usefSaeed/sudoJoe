from services.Prover.zkProverService import ZKProverService


class ColouringProver(ZKProverService):
    def __init__(self, gameIndex):
        super().__init__(gameIndex)

    def prove(self):
        pass