from frontend.frontendGlobal import salty_sha256

class VerifierCell:
    __VALID_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, None]

    def __init__(self, value=None):
        self.__isFilledIn = value is not None
        self.__set(value)
        self.__commitment = None
        self.__nonce = None

    def __str__(self):
        return str(self.__value) if self.__value is not None else "_"

    def __int__(self):
        return self.__value if self.__value is not None else 0

    def __set(self, new_value):
        if new_value in self.__VALID_VALUES:
            self.__value = new_value
        else:
            raise ValueError("Invalid value for SudokuCell")

    def is_empty(self):
        return self.__value is None

    def save_commitment(self,c):
        self.__commitment = c

    def verify_commitment(self,value_nonce_pair):
        value = value_nonce_pair[0]
        nonce = value_nonce_pair[1]
        return value if salty_sha256(value,nonce) == self.__commitment else 0

    def is_filled_in(self):
        return self.__isFilledIn

    def get_real_value(self):
        return self.__value
