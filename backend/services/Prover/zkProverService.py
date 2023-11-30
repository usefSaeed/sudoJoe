from backend.model.board import Board
from backend.globalData import readJSON,game_path


class ZKProverService:
    def __init__(self, gameIndex):
        game_data = readJSON(game_path(gameIndex))
        self._game = Board(game_data['value'])
        self._solution = self._game.extract_solution(game_data['solution'])


# zs = ZKProverService(3)

