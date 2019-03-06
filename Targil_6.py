def main():
    ls = [1, 2, 3]
    mapping(add, ls)
    print(ls)


def mapping(f, ls):
    for i in range(len(ls)):
        ls[i] = f(ls[i])


def add(x):
    return x + 2


if __name__ == '__main__':
    main()