
class ATM:
    def __init__(self, secretCode = 123456, amountOfMoney = 3000):
        self._secretCode = secretCode
        self._amountOfMoney = amountOfMoney

    def secertCodeCheck(self,secretCode):
        if secretCode == self._secretCode:
            return True
        return False

    







