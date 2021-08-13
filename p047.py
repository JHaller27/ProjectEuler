import utils.eulerlib as EL
from itertools import count


def main():
    target = 4
    chain = 0

    for n in count(4):
        primes = list(EL.prime_factor_generator(n))
        distinct_primes = len(set(primes))

        if distinct_primes == target:
            chain += 1
        else:
            chain = 0

        if chain == target:
            return n - target + 1


if __name__ == "__main__":
    ans = main()
    print(ans)
