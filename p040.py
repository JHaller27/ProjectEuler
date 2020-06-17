import itertools
import utils.moreitertools as moreitertools


def digits():
    yield 0
    for num in itertools.count(1):
        digs = []
        while num > 0:
            digs.append(num % 10)
            num //= 10
        for d in reversed(digs):
            yield d


def main():
    product = 1
    for d in moreitertools.itake_many(digits(), map(lambda p: 10**p, range(6+1))):
        print(d)
        product *= d

    return product


if __name__ == '__main__':
    ans = main()
    print(ans)
