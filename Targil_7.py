

def caching_initialize_structure(function):
    cache_stock = dict()

    def caching(*args):
        if args in cache_stock:
            return cache_stock[args]
        else:
            result = function(*args)
            cache_stock[args] = result
            return result

    return caching


if __name__ == '__main__':
    main()