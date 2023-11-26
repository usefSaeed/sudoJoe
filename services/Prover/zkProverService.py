import json
from model.board import Board

GAMES_DIRECTORY = "..\games"

from globalData import *


class ZKProverService:
    def __init__(self, gameIndex):
        with open(game_path(gameIndex), 'r') as file:
            game_data = json.load(file)
        self._currentBoard = Board(game_data['value'])
        self._solution = Board(game_data['solution'])
        self._solution.show()

zs = ZKProverService(3)
