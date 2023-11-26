class Cell:
    valid_values = {1, 2, 3, 4, 5, 6, 7, 8, 9, None}

    def __init__(self, value=None):
        if value in self.valid_values:
            self.value = value
        else:
            raise ValueError("Invalid value for SudokuCell")

    def __str__(self):
        return str(self.value)

    def is_empty(self):
        return self.value is None

    def set(self,new_value):
        self.value = new_value