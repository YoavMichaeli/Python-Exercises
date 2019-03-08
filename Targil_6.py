def main():
    ls = [1, 2, 3]
    mapping(add, ls)
    print(ls)


def mapping(f, ls):
    """
    The function receives a function and a list and
    runs the function with the list as an input.
    :param f: a pointer to function
    :param ls: a list which sends as an input to f function
    :return:
    """
    for i in range(len(ls)):
        ls[i] = f(ls[i])


def add(x):
    """
    The function receives as an input a number, add to it 2 and returns
    the result.
    :param x: the number which the function receives
    :return: x +2
    """
    return x + 2


if __name__ == '__main__':
    main()