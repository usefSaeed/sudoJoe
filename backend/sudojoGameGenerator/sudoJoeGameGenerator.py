import json
import time
import requests
from backend.backendGlobal import GAMES_DIRECTORY


API_LIMIT = 20
API = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:20){grids{value,solution,difficulty}}}"

def getGames(relative_path,required_games_count,games_already_generated=0):
    for itr in range(required_games_count//API_LIMIT):
        response = requests.get(API)
        response = response.json()['newboard']['grids']
        for i,r in enumerate(response):
            file_path = relative_path + str(games_already_generated + i + API_LIMIT*itr)
            with open(file_path, "w") as file:
                file.write(json.dumps(r))
            print(file_path,"done")
    time.sleep(5)

getGames(GAMES_DIRECTORY,100)
