from backend.model.sudoJoeBoard import SudoJoeBoard
from backend.backendGlobal import readJSON,game_path


class ZKProverService:
    def __init__(self, gameIndex):
        game_data = readJSON(game_path(gameIndex))
        self._game = SudoJoeBoard()
        self._game.fill_from_file(game_data['value'])
        self._solution = self._game.extract_solution(game_data['solution'])


# zs = ZKProverService(3)

