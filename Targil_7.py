def main():
        print(fibonacci(310))
        print(fibonacci(300))
        print(fibonacci(300))
        print(fibonacci(290))


def caching_initialize_structure(function):
    """
    This function creates a dictionary for caching function results.
    :param function: generic function which needs to cache heavy calculating results.
    :return: caching function value(the returned value of the decorated function which received)
    """
    # Creating a dictionary caching stock
    cache_stock = dict()

    def caching(*args):
        """
        The function checks in the dictionary if it has the result of the inserted
        arguments to the decorated function.
        :param args: the input which received by the decorated function
        :return: decorated function return value
        """
        # Checking if the argument is in the dictionary, if it is return it.
        if args in cache_stock:
            return cache_stock[args]
        else:
            # The argument is not found, calculating the result and storing it in the dictionary.
            result = function(*args)
            cache_stock[args] = result
            return result

    return caching


@caching_initialize_structure
def fibonacci(n):
    """
    Fibbonachi function receives an index and finds his value in Fibonacci sequence.
    :param n: an index in fibonacci sequence.
    :return: index's value
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    main()