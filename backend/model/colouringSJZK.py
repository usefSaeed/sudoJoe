from backend.model.sudoJoeZK import SudoJoeZK


class ColouringSJZK(SudoJoeZK):
    verifying_options_count = 28

    def __init__(self, gameInt, fiatShaIdx,committedSolution,revealedCells):
        super().__init__(gameInt, fiatShaIdx)
        self._committedSolution = committedSolution
        self._revealedCells = revealedCells
