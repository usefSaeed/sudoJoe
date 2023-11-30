from backend.model.sudoJoeZK import SudoJoeZK


class ColouringSJZK(SudoJoeZK):
    def __init__(self, gameInt, fiatShaIdx,committedSolution):
        super().__init__(gameInt, fiatShaIdx)
        self._committedSolution = committedSolution
