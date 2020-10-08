import itertools
import utils.primes as primes


def pandigitals(n):
    for digits in itertools.permutations(range(n, 0, -1)):
        num = 0
        for d in digits:
            num = num * 10 + d
        yield num


def main():
    return max([max(filter(primes.is_prime, pandigitals(n)), default=0) for n in range(9, 3, -1)])


if __name__ == "__main__":
    ans = main()
    print(ans)
