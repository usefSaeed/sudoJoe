import copy
import hashlib
import json
import math
import os
import functools
import operator
from numpy import random
import random as r

GAME_SIDE_LENGTH = 9
SUBGRID_SIDE_LENGTH = 3
ROW = 0
COL = 1
SUBGRID = 2
TYPE_COUNT = 3
GAMES_DIRECTORY = "C:\#MY Stuff\sudoJoe\\backend\games"
PROOFS_TEMP_DIRECTORY = "C:\#MY Stuff\sudoJoe\\frontend\proofs"


def game_path(gameIndex):
    return GAMES_DIRECTORY + "\\" + str(gameIndex)


def generate_nonce():
    return r.randint(0, 2 ** 256 - 1)


def salty_sha256(value, nonce):
    data = {
        "value": value,
        "nonce": nonce,
    }
    return hashlib.sha3_256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def permute(arr):
    random.shuffle(arr)


def readJSON(path):
    with open(path, 'r') as file:
        return json.load(file)

def writeJSON(path,content):
    with open(path, 'w') as json_file:
        json.dump(content,json_file,indent=4)

def get_files_from_dir(path):
    return [_ for _ in os.listdir(path)]


def random_pick(arr):
    return random.choice(arr)


def copy_object(obj):
    return copy.deepcopy(obj)


def xor_all_mod_n(hashes,n):
    hex_hashes = [int(h, 16) for h in hashes]
    num = (functools.reduce(operator.xor, hex_hashes)) % n
    return num


def pseudo_random_num(seed):
    return random.RandomState(seed)


def get_exponent(m,n_power_e):
    e = math.ceil(math.log(m,n_power_e))
    return e


def get_proof_path(gameIndex,proofIndex):
    return f"{PROOFS_TEMP_DIRECTORY}\\game-{gameIndex}-zkp-{proofIndex}.json"

def get_game_vpath(gameIndex):
    return f"{PROOFS_TEMP_DIRECTORY}\\game-{gameIndex}.json"