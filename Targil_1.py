def main():
    atm = ATM('1234', 10000)
    start_atm_machine(atm)


def start_atm_machine(atm):
    """
    Starting atm machine to serve clients.
    The function operates all atm's functions and repeats the process until the
    customer wants to quit.
    :param atm: An ATM object which needs to serve a client.
    :return:
    """
    while True:
        code_number = input("Welcome to ATM services!\n"
                            "Please enter secret code number: **** \n")
        valid = atm.secret_code_check(code_number)
        if valid is True:
            atm.print_menu()
            # Taking customer choice and making his decision.
            customer_choice = input()
            if customer_choice == '1':
                atm.print_amount_of_money()
                continue
            elif customer_choice == '2':
                atm.withdraw_money()
                continue
            elif customer_choice == '3':
                atm.change_secret_code()
                continue
            elif customer_choice == '4':
                print("Thank you for choosing our ATM services, good bye!")
                break
            else:
                print("Wrong input!\n")
                atm.print_amount_of_money()
                continue

        else:
            print("Wrong code number!\n")


class ATM:

    def __init__(self, secret_code, amount_of_money):
        """
        Initialize function of class ATM
        :param secret_code: the secret code number of the client(default 1234)
        :param amount_of_money: the amount of money of the client(default 3000$)
        """
        self._secret_code = secret_code
        self._amount_of_money = amount_of_money

    def secret_code_check(self, secret_code):
        """
        The function checks if the secret code is valid
        :param secret_code: The user input secret code number
        :return: True - if there is a match, False - no match.
        """
        if secret_code == self._secret_code:
            return True
        return False

    def print_menu(self):
        """
        Printing ATM menu
        :return:
        """
        print("\n{0}\n{1}\n{2}\n{3}\n{4}".format("Welcome to your customer account!",
                                                 "Press 1 to print your account balance",
                                                 "Press 2 to withdraw money from your account",
                                                 "Press 3 to change your secret code number",
                                                 "Press 4 to exit"))

    def print_amount_of_money(self):
        """
        Printing the amount of money in the current account
        :return:
        """
        print("{0}{1}\n".format("Account balance is: ", self._amount_of_money))

    #
    def withdraw_money(self):
        """
        Withdraw money from the current account, the client can withdraw
        20$, 50$ or other amount if he has enough money in the account.
        :return:
        """
        current_amount_of_money = self._amount_of_money
        # Checking whether there is money in the account
        if self._amount_of_money == 0:
            print("You don't have money in your account.\n")
            return
        self.withdraw_money_menu()
        # Taking customer choice checking if it is possible and performing the action.
        customer_choice = input()
        if customer_choice == '1' and self._amount_of_money - 20 >= 0:
            self._amount_of_money -= 20
        elif customer_choice == '2' and self._amount_of_money - 50 >= 0:
            self._amount_of_money -= 50
        elif customer_choice == '3':
            other_amount = int(input("Enter other amount to withdraw: "))
            if self._amount_of_money - other_amount >= 0:
                self._amount_of_money -= other_amount
        # Checking if an action has made - means that the transaction made successfully.
        if self._amount_of_money < current_amount_of_money:
            print("Money withdrawal has been made successfully!\n")
        elif customer_choice in ['1', '2', '3']:
            print("You don't have enough money to make this transaction.\n")
        else:
            print("Wrong input!\n")

    def withdraw_money_menu(self):
        """
        Printing the withdrawal menu
        :return:
        """
        print("{0}\n{1}\n{2}\n{3}".format("Please choose an amount of money to withdraw:",
                                          "Press 1 to withdraw 20$",
                                          "Press 2 to withdraw 50$",
                                          "Press 3 to withdraw other amount"))

    def change_secret_code(self):
        """
        Changing secret code of the current account.
        :return:
        """
        new_code = input("Enter new secret code: ")
        valid_flag = self.secret_code_input_check(new_code)
        if valid_flag is False:
            print("Wrong input, changing secret code has been failed!\n")
            return
        self._secret_code = new_code
        print("New secret code has been changed successfully!\n")

    def secret_code_input_check(self, secret_code):
        """
        Checking secret code input's validity
        :param secret_code: The input which received by the client.
        :return: True - the secret code is valid, False - not valid.
        """
        # Checking if the secret code length equals 4
        if len(secret_code) == 4:
            # Checking if the secret code contains only digits.
            if secret_code.isdigit() is False:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    main()










