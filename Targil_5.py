def main():
    id_number = input("Enter an id with 9 digits please :\n")
    valid = check_id(id_number)





def valid_id_length(id_num):
    if len(id_num) != 9:
        return False
    else:
        return True

if __name__ == '__main__':
    main()