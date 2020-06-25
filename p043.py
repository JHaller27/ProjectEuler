import itertools
from functools import reduce


def pandigitals():
    for digs in itertools.permutations(range(10),  10):
        yield reduce(lambda acc, e: acc * 10 + e, digs)


def is_substring_divisible(num):
    prime_itr = iter([17, 13, 11, 7, 5, 3, 2])

    while num > 1000:
        sub = num % 1000
        if sub % next(prime_itr) != 0:
            return False
        num //= 10

    return True


def main():
    return sum(filter(is_substring_divisible, pandigitals()))


if __name__ == '__main__':
    ans = main()
    print(ans)

