from backend.model.proverBoard import ProverBoard
from backend.backendGlobal import get_files_from_dir,GAMES_DIRECTORY,random_pick,readJSON,game_path


class gameService:
    def __init__(self):
        self._diff = None
        self._solution = None
        self._currentBoard = None
        self._currentGameIndex = None

    def generate_random_game(self):
        games = get_files_from_dir(GAMES_DIRECTORY)
        random_game_file = random_pick(games)
        self._currentGameIndex = int(random_game_file)
        self._extract_game()
        return self._currentBoard

    def _extract_game(self):
        game_data = readJSON(game_path(self._currentGameIndex))
        self._currentBoard = ProverBoard()
        self._currentBoard.fill_from_file(game_data['value'])
        self._diff = game_data['difficulty']
        self._currentBoard.show()

    def get_game_index(self):
        return self._currentGameIndex


gs = gameService()
gs.generate_random_game()