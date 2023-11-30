import copy
import hashlib
import random
import json
import os

GAME_SIDE_LENGTH = 9
SUBGRID_SIDE_LENGTH = 3
GAMES_DIRECTORY = "D:\Projects\sudoJoe\\backend\games"


def game_path(gameIndex):
    return GAMES_DIRECTORY + "\\" + str(gameIndex)


def generate_nonce():
    return random.randint(0, 2 ** 256 - 1)


def salty_sha256(value, nonce):
    data = {
        "value": value,
        "nonce": nonce,
    }
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def salty_sha256_mod(value, nonce, n):
    hash_value = salty_sha256(value, nonce)
    return int(hash_value, 16) % n


def permute(arr):
    random.shuffle(arr)


def readJSON(path):
    with open(path, 'r') as file:
        return json.load(file)


def get_files_from_dir(path):
    return [_ for _ in os.listdir(path)]


def random_pick(arr):
    return random.choice(arr)


def copy_object(obj):
    return copy.deepcopy(obj)
