import os
import random
import json
from model.board import Board
from globalData import *


class gameService:
    def __init__(self):
        self._diff = None
        self._solution = None
        self._currentBoard = None
        self._currentGameIndex = None

    def generate_random_game(self):
        games = [g for g in os.listdir(GAMES_DIRECTORY)]
        random_game_file = random.choice(games)
        self._currentGameIndex = int(random_game_file)
        self._extract_game()
        return self._currentBoard

    def _extract_game(self):
        with open(game_path(self._currentGameIndex), 'r') as file:
            game_data = json.load(file)
        self._currentBoard = Board(game_data['value'])
        self._diff = game_data['difficulty']
        self._currentBoard.show()

    def get_game_index(self):
        return self._currentGameIndex


gs = gameService()
gs.generate_random_game()