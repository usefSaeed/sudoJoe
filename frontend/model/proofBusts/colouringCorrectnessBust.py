class ColouringCorrectnessBust:
    ROW = 0
    COL = 1
    SUBGRID = 2
    FILLED_IN = 3

    def __init__(self,type,idx=None):
        self.__errorType = type
        self.__idx = idx

    def __str__(self):
        match self.__errorType:
            case self.ROW:
                return f"Row {self.__idx} has non-distinct true values"
            case self.COL:
                return f"Column {self.__idx} has non-distinct true values"
            case self.SUBGRID:
                return f"Subgrid {self.__idx} has non-distinct true values"
            case self.FILLED_IN:
                return f"Permutation is non-consistent with original game"
