def main():
    atm = ATM()
    while True:
        code_number = input("Please enter secret code number:\n")
        print(" ")
        valid = atm.secret_code_check(code_number)
        if valid is True:
            atm.print_menu()
            customer_choice = int(input())
            if customer_choice == 1:
                atm.print_amount_of_money()
                continue
            elif customer_choice == 2:
                atm.withdraw_money()
                continue

        else:
            print("Wrong code number!")


class ATM:
    def __init__(self, secret_code=123456, amount_of_money=3000):
            self._secret_code = secret_code
            self._amount_of_money = amount_of_money

    def secret_code_check(self, secret_code):
            if int(secret_code) == self._secret_code:
                return True
            return False

    def print_menu(self):
        print("\n{0}\n{1}\n{2}\n{3}\n{4}".format("Welcome to your account customer!",
                                                 "Press 1 to print your account balance",
                                                 "Press 2 to withdraw money from your account",
                                                 "Press 3 to change your secret code number",
                                                 "Press 4 to exit"))

    def print_amount_of_money(self):
            print("{0}{1}".format("Account balance is: ", self._amount_of_money))

    def withdraw_money(self):
        self.withdraw_money_menu()
        customer_choice = int(input())
        if customer_choice == 1:
            self._amount_of_money -= 20
        elif customer_choice == 2:
            self._amount_of_money -= 50
        else:
            other_amount = int(input("Enter other amount to withdraw: "))
            self._amount_of_money -= other_amount
        print("Money withdrawal has been made successfully!")

    def withdraw_money_menu(self):
        print("{0}\n{1}\n{2}\n{3}".format("Please choose an amount of money to withdraw:",
                                          "Press 1 to withdraw 20$",
                                          "Press 2 to withdraw 50$",
                                          "Press 3 to withdraw other amount"))


if __name__ == '__main__':
    main()










