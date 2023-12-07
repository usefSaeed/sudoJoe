from backend.model.proverBoard import ProverBoard
from backend.backendGlobal import readJSON,game_path,get_game_vpath,writeJSON


class ZKProverService:
    def __init__(self, gameIndex):
        gameData = readJSON(game_path(gameIndex))
        self._game = ProverBoard()
        self._game.fill_from_file(gameData['value'])
        writeJSON(get_game_vpath(gameIndex), gameData['value'])
        self._solution = self._game.extract_solution(gameData['solution'])




# zs = ZKProverService(3)

