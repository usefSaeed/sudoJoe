class Cell:
    valid_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, None}

    def __init__(self, value=None,row=0,col=0):
        if value in self.valid_values:
            self.__value = value
        else:
            raise ValueError("Invalid value for SudokuCell")
        self.__row = row
        self.__col = col

    def __str__(self):
        return str(self.__value)

    def __int__(self):
        return self.__value

    def is_empty(self):
        return self.__value is None

    def set(self, new_value):
        self.__value = new_value

