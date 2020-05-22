import itertools
from utils.decorators import *


FIRST_FIBS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

@memoize()
def fib(n: int) -> int:
    if n < len(FIRST_FIBS):
        return FIRST_FIBS[n]

    return fib(n - 1) + fib(n - 2)


def main():
    for n in itertools.count(12):
        if len(str(fib(n))) == 1000:
            return n

        if len(str(fib(n))) > 1000:
            return None


if __name__ == '__main__':
    ans = main()
    print(ans)
