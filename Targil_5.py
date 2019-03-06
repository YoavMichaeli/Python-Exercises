def main():
    id_number = input("Enter an id with 9 digits please :\n")
    check_id(id_number)


def check_id(id_num):
    """
    The function checks if id_num is a valid number.
    :param id_num:
    :return:
    """
    # Checks if the id has the right length.
    if valid_id_length(id_num):
        # Splitting the list and parsing to int.
        digit_list = list(map(int, list(id_num)))
        sum_digits = sum_digits_list(digit_list)
        closest_tenth = round(sum_digits, -1)
        # Checking if the last digit in the id is correct.
        if abs(closest_tenth - sum_digits) == digit_list[-1]:
            print("The ID is valid!")
            return
    print("The ID is not valid")


def sum_digits_list(digit_list):
    """
    The function calculates the sum of the digits in the list
    according to the way it needs to be calculate and returns
    the sum.
    :param digit_list:
    :return: sum_digit
    """
    temp = 2
    mul_by = 1
    sum_digits = 0
    for digit in digit_list[:8]:
        # Checking if the calculation is not a two digits number
        if len(str(digit * mul_by)) != 1:
            digit = sum(map(int, str(digit * mul_by)))
            sum_digits += digit
        else:
            sum_digits += digit * mul_by
        mul_by, temp = temp, mul_by
    return sum_digits


def valid_id_length(id_num):
    """
    The function checks if id_num length equals 9.
    :param id_num:
    :return: False - if id_num doesn't have 9 digits, True - if it has.
    """
    if len(id_num) != 9:
        return False
    else:
        return True


if __name__ == '__main__':
    main()