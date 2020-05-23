import itertools


POWER = 5


def build_number(digits: tuple) -> int:
    return sum(map(lambda t: t[1] * 10**t[0], enumerate(reversed(digits))))


def fifth_powers():
    for num_digits in itertools.takewhile(lambda n: 10**(n-1) - 1 <= n * 9 ** POWER, itertools.count(2)):
        for operands in itertools.product(*([range(10)] * num_digits)):
            num = build_number(operands)
            if sum(map(lambda e: e**POWER, operands)) == num and operands[0] != 0:
                yield num


def main():
    return sum(fifth_powers())


if __name__ == '__main__':
    ans = main()
    print(ans)
