from backend.backendGlobal import generate_nonce,salty_sha256

class ProverCell:
    __VALID_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, None]

    def __init__(self, value=None):
        self.__isOriginallyFilledIn = value is not None
        self.set(value)
        self.__commitment = None
        self.__nonce = None

    def __str__(self):
        return str(self.__value) if self.__value is not None else "_"

    def __int__(self):
        return self.__value if self.__value is not None else 0

    def set(self, new_value):
        if new_value in self.__VALID_VALUES:
            self.__value = new_value
        else:
            raise ValueError("Invalid value for SudokuCell")

    def is_empty(self):
        return self.__value is None

    def commit_cell(self):
        self.__nonce = generate_nonce()
        self.__commitment = salty_sha256(self.__value,self.__nonce)
        return self.__commitment

    def reveal_cell(self):
        return self.__value,self.__nonce

    def is_originally_filled_in(self):
        return self.__isOriginallyFilledIn
