def main():
    sum_numbers_faster()


def sum_numbers():
    sum_of_numbers = 0
    first_number_flag = False
    while True:
        number = input("Enter a number, to stop please write - 'stop'  : \n")
        if number == "stop":
            if first_number_flag is False:
                print("The user didn't enter any number.")
            else:
                print("{0}{1}".format("The sum is: ", sum_of_numbers))
            break
        else:
            first_number_flag = True
            sum_of_numbers += int(number)


def sum_numbers_faster():
    numbers = input("Please enter all numbers with a comma between each number and then press enter: \n")
    numbers = numbers.split(',')
    numbers = list(map(int, numbers))
    print("The sum is : ", end=str(sum(numbers)))


if __name__ == '__main__':
    main()