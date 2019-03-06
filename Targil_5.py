def main():
    id_number = input("Enter an id with 9 digits please :\n")
    check_id(id_number)


def check_id(id_num):
    if valid_id_length(id_num):
        digit_list = list(map(int, list(id_num)))
        sum_digits = sum_digits_list(digit_list)
        closest_tenth = round(sum_digits, -1)
        if abs(closest_tenth - sum_digits) == digit_list[-1]:
            print("The ID is valid!")
            return
    print("The ID is not valid")


def sum_digits_list(digit_list):
    temp = 2
    mul_by = 1
    sum_digits = 0
    for digit in digit_list[:8]:
        if len(str(digit * mul_by)) != 1:
            digit = sum(map(int, str(digit * mul_by)))
            sum_digits += digit
        else:
            sum_digits += digit * mul_by
        mul_by, temp = temp, mul_by
    return sum_digits


def valid_id_length(id_num):
    if len(id_num) != 9:
        return False
    else:
        return True


if __name__ == '__main__':
    main()