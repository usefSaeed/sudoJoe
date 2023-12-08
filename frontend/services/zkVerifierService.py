from frontend.model.boards.verifierBoard import VerifierBoard
from frontend.frontendGlobal import readJSON,get_game_vpath


class ZKVerifierService:
    def __init__(self, gameIndex):
        gameData = readJSON(get_game_vpath(gameIndex))
        self._game = VerifierBoard()
        self._game.fill_from_file(gameData)


