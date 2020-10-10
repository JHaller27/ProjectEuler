import itertools


def i2d(i):
    d = {}
    while i > 0:
        dig = i % 10
        if dig not in d:
            d[dig] = 1
        else:
            d[dig] += 1
        i //= 10
    return d


def main():
    for i in itertools.count(2):
        if i2d(i) == i2d(2*i) == i2d(3*i) == i2d(4*i) == i2d(5*i) == i2d(6*i):
            return i


if __name__ == "__main__":
    ans = main()
    print(ans)
