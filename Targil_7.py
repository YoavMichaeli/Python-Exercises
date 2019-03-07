def main():
    for i in range(2):
        print(fibonacci(4))
        print("***\n")


def caching_initialize_structure(function):
    cache_stock = dict()

    def caching(*args):
        if args in cache_stock:
            print(args)
            print("Found")
            return cache_stock[args]
        else:
            print(args)
            print("Not found")
            result = function(*args)
            cache_stock[args] = result
            print(cache_stock)
            return result

    return caching


@caching_initialize_structure
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    main()