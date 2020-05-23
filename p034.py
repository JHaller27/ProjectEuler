from utils.decorators import *
import itertools


def build_number(digits: tuple) -> int:
    return sum(map(lambda t: t[1] * 10**t[0], enumerate(reversed(digits))))


@memoize()
def fact(n):
    if n <= 1:
        return 1

    return n * fact(n-1)


def factorials():
    for num_digits in itertools.takewhile(lambda n: 10**n - 1 <= fact(9) * n, itertools.count(2)):
        for operands in itertools.product(range(1, 10), *([range(10)] * (num_digits - 1))):
            num = build_number(operands)
            if sum(map(fact, operands)) == num and operands[0] != 0:
                yield num


def main():
    return sum(factorials())


if __name__ == '__main__':
    ans = main()
    print(ans)
