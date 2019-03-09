def main():
    sum_numbers_faster()


def sum_numbers():
    """
    The function receives numbers from the user,
    summarize them and print the sum.
    :return:
    """
    sum_of_numbers = 0
    first_number_flag = False
    while True:
        number = input("Enter a number, to stop please write - 'stop'  : \n")
        # Checking if the user wanted to stop
        if number == "stop":
            # Checking if the user entered al least one number.
            if first_number_flag is False:
                print("The user didn't enter any number.")
            else:
                print("{0}{1}".format("The sum is: ", sum_of_numbers))
            break
        else:
            # A number has received
            first_number_flag = True
            # Summarizing number
            sum_of_numbers += int(number)


def sum_numbers_faster():
    """
    The function receives in one time numbers as one string,
    summarize them and print the sum.
    :return:
    """
    numbers = input("Please enter all numbers with a comma between each number and then press enter: \n")
    # Splitting the input from the user to a list of numbers as str type.
    numbers = numbers.split(',')
    # Turning the str list to list of integers
    numbers = list(map(int, numbers))
    # Summarizing the list with sum function
    print("The sum is : ", end=str(sum(numbers)))


if __name__ == '__main__':
    main()