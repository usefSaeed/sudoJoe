from backend.services.colouringProver import ColouringProver
from frontend.services.colouringVerifier import ColouringVerifier

GAME_INDEX = 1
cpzk = ColouringProver(GAME_INDEX)
proofSize = cpzk.prove(tolerable_perc=0.005)
cvzk = ColouringVerifier(GAME_INDEX,proofSize)
cvzk.verify()
