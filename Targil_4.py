def main():
    s = "aaabbcbbbanns"
    print(shrink_string(s))


def shrink_string(s):
    temp_string = ""
    count_repeats = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            temp_string += s[i] + str(count_repeats)
            count_repeats = 1
        else:
            count_repeats += 1
    temp_string += s[i+1] + str(count_repeats)
    return temp_string


if __name__ == '__main__':
    main()