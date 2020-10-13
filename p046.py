import utils.primes as primes
import itertools


SMALLEST_PRIME = 2
SMALLEST_DOUBLED_SQUARE = 2

known_goldbach_nums = set()
def is_goldbach_num(n):
    if n in known_goldbach_nums:
        return True

    for p in primes.primes(n - SMALLEST_DOUBLED_SQUARE + 1):
        if p % 2 == 0:
            continue

        for ds in map(lambda x: 2*(x**2), itertools.count(1)):
            x = p + ds

            known_goldbach_nums.add(x)

            if x > n:
                break

            if x == n:
                return True

    return False


def main():
    for x in itertools.count(9, 2):
        if not primes.is_prime(x) and not is_goldbach_num(x):
            return x


if __name__ == "__main__":
    ans = main()
    print(ans)
