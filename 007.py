import itertools


def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    for d in range(3, int(n**.5) + 1):
        if n % d == 0:
            return False

    return True


if __name__ == '__main__':
    print(next(itertools.islice(filter(is_prime, itertools.count(2)), 10000, 10001)))
