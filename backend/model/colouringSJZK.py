from backend.model.sudoJoeZK import SudoJoeZK
from backend.globalData import salty_sha256_mod,GAME_SIDE_LENGTH


class ColouringSJZK(SudoJoeZK):
    verifying_options_count = 28

    def __init__(self, gameInt, fiatShaIdx,committedSolution,revealedCells):
        super().__init__(gameInt, fiatShaIdx)
        self._committedSolution = committedSolution
        self._revealedCells = revealedCells
