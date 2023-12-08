import copy
import hashlib
import json
import math
import os
import functools
import operator
import glob
from numpy import random

GAME_SIDE_LENGTH = 9
SUBGRID_SIDE_LENGTH = 3
ROW = 0
COL = 1
SUBGRID = 2
TYPE_COUNT = 3
PROOFS_TEMP_DIRECTORY = "C:\#MY Stuff\sudoJoe\\frontend\proofs\\"

def salty_sha256(value, nonce):
    data = {
        "value": value,
        "nonce": nonce,
    }
    return hashlib.sha3_256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def readJSON(path):
    with open(path, 'r') as file:
        return json.load(file)


def get_files_from_dir(path):
    return [_ for _ in os.listdir(path)]


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

def get_proof_title(gameIndex,proofIndex):
    return f"game-{gameIndex}-zkp-{proofIndex}"

def get_proof_path(gameIndex,proofIndex):
    return f"{PROOFS_TEMP_DIRECTORY}{get_proof_title(gameIndex,proofIndex)}.json"

def get_game_vpath(gameIndex):
    return f"{PROOFS_TEMP_DIRECTORY}game-{gameIndex}.json"

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except Exception:
        pass


def delete_all_files(directory):
    try:
        files = glob.glob(os.path.join(directory, '*'))
        for file in files:
            delete_file(file)
    except Exception:
        pass

