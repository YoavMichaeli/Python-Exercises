def main():
    s = "aaabbcbbbanns"
    print(shrink_string(s))


def shrink_string(s):
    """
    The function shrinks the string for example:
    aaabbbc will turn to -> a3b3c1
    :param s: A string to shrink
    :return: temp_string - the new shrink string
    """
    # This variable will contain the shrink string.
    temp_string = ""
    # count_repeats contains how many times a character repeats in the string.
    count_repeats = 1
    for i in range(len(s)-1):
        # If a character is equal to the character before we can continue.
        if s[i] != s[i+1]:
            temp_string += s[i] + str(count_repeats)
            count_repeats = 1
        else:
            count_repeats += 1
    # Taking care of the last character.
    temp_string += s[i+1] + str(count_repeats)
    return temp_string


if __name__ == '__main__':
    main()