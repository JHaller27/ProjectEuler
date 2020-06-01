import itertools
from utils.primes import is_prime, primes


def rotate(num: int) -> int:
    yield num
    snum = str(num)

    itr = itertools.cycle(snum)
    for _ in range(len(snum) - 1):
        next(itr)
        yield int(''.join(next(itr) for _ in range(len(snum))))


def is_circular_prime(num: int) -> bool:
    for rotation in rotate(num):
        if not is_prime(rotation):
            return False

    return True


def main():
    LIMIT = 10**6
    return len(list(filter(is_circular_prime, primes(end=LIMIT))))


if __name__ == '__main__':
    ans = main()
    print(ans)
