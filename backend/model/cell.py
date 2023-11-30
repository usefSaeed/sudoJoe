from backend.globalData import generate_nonce,salty_sha256

class Cell:
    valid_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, None}

    def __init__(self, value=None,row=0,col=0):
        self.__isOriginallyFilledIn = value is not None
        self.__set_all(value,row,col)
        self.__commitment = None
        self.__nonce = None

    def __str__(self):
        return str(self.__value) if self.__value is not None else "_"

    def __int__(self):
        return self.__value if self.__value is not None else 0

    def set(self, new_value):
        if new_value in self.valid_values:
            self.__value = new_value
        else:
            raise ValueError("Invalid value for SudokuCell")

    def __set_all(self, new_value, row, col):
        self.set(new_value)
        if row in self.valid_values[:-1] and col in self.valid_values[:-1]:
            self.__row = row
            self.__col = col
        else:
            raise ValueError("Invalid cell coordinates for SudokuCell")

    def is_empty(self):
        return self.__value is None

    def get_coordinates(self):
        return self.__row,self.__col

    def commit_cell(self):
        self.__nonce = generate_nonce()
        self.__commitment = salty_sha256(self.__value,self.__nonce)
        return self.__commitment

    def reveal_cell(self):
        return self.__value,self.__nonce

    def is_originally_filled_in(self):
        return self.__isOriginallyFilledIn



