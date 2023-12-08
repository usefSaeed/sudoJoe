from frontend.frontendGlobal import salty_sha256


class CommitmentBust:
    def __init__(self,row,col,value_nonce_pair,commitment):
        self.__row = row
        self.__col = col
        self.__value = value_nonce_pair[0]
        self.__nonce = value_nonce_pair[1]
        self.__commitment = commitment

    def __str__(self):
        return f"Wrong commitment at [{self.__row}][{self.__col}]\n" \
               f"Revealed Value : {self.__value}\n" \
               f"Revealed Nonce : {self.__nonce}\n" \
               f"Expected Commitment : {salty_sha256(self.__value,self.__nonce)}\n" \
               f"Actual Commitment   : {self.__commitment}"
