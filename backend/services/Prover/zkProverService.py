from backend.model.board import Board

GAMES_DIRECTORY = "..\\..\\games\\"

from backend.globalData import *


class ZKProverService:
    def __init__(self, gameIndex):
        game_data = readJSON(game_path(gameIndex))
        self._game = Board(game_data['value'])
        self._solution = Board(game_data['solution'])


# zs = ZKProverService(3)

