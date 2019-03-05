def main():
    atm = ATM()
    while True:
        codeNumber = input("Please enter secret code number:")
        valid = atm.secertCodeCheck(codeNumber)
        if valid is True:
            atm.printMenu()
            customerChoice = input()
            customerChoice = int(customerChoice)
            if customerChoice == 1:
                atm.printAmountOfMoney()
        else:
            print("Wrong code number!")



class ATM:
    def __init__(self, secretCode = 123456, amountOfMoney = 3000):
            self._secretCode = secretCode
            self._amountOfMoney = amountOfMoney

    def secertCodeCheck(self,secretCode):
            if int(secretCode) == self._secretCode:
                return True
            return False

    def printMenu(self):
        print("{0}\n{1}\n{2}\n{3}\n{4}".format("Welcome to your account customer!",
                                               "Press 1 to print your account balance",
                                               "Press 2 to withdraw money from your account",
                                               "Press 3 to change your secret code number",
                                               "Press 4 to exit"))

    def printAmountOfMoney(self):
            print("{0}{1}".format("Account balance is: ", self._amountOfMoney))


if __name__ == '__main__':
    main()










