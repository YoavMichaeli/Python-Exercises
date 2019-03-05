def main():
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    winner = win_check(game)
    if winner:
        print("The winner is player number: ", end=str(winner))
    else:
        print("This is a tie!")


def make_slants_list(games):
    """
    making a list of all the possible slants
    to check who is the winner.
    :param games:
    :return:
    """
    first_slant = []
    second_slant = []
    for i in range(3):
        first_slant.append(games[i][i])

    for z, j in zip(range(2, -1), range(3)):
        second_slant.append(games[z][j])

    games.append(first_slant)
    games.append(second_slant)


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