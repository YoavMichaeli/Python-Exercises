def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    winner = win_check(game)
    if winner:
        print("The winner is player number: ", end=str(winner))
    else:
        print("This is a tie!")


def check_identical_items_list(ls):
    """
    counting if a number repeats 3 times to check winning.
    :param ls:
    :return: 1 - if number 1 won, 2 - if number 2 won, 0 - if no one won yet
    """
    if ls.count(1) == 3:
        return 1
    elif ls.count(2) == 3:
        return 2
    else:
        return 0


if __name__ == '__main__':
    main()