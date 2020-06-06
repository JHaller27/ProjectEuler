import cProfile
import itertools
import utils.primes as primes


def is_truncatable(num: int) -> bool:
    if not primes.is_prime(num):
        return False

    mult = 10
    while mult < num:
        if not primes.is_prime(num % mult) or not primes.is_prime(num // mult):
            return False
        mult *= 10

    return True


def main():
    return sum(itertools.islice(filter(is_truncatable, itertools.count(11)), 11))


if __name__ == '__main__':
    ans = main()
    print(ans)
