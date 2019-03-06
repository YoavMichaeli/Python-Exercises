def main():
    ls = [1, 2, 3]
    mapping(add, ls)
    print(ls)


def mapping(f, ls):
    """
    The function receives a function and a list and
    runs the function with the list as an input.
    :param f:
    :param ls:
    :return:
    """
    for i in range(len(ls)):
        ls[i] = f(ls[i])


def add(x):
    """
    The function gets as an input a number, add to it 2 and returns
    the result.
    :param x:
    :return: x +2
    """
    return x + 2


if __name__ == '__main__':
    main()