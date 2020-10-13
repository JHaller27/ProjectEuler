from typing import Iterator
import itertools

PRIMES = []

with open('./data/primes.txt', 'r') as fin:
    for line in fin:
        PRIMES.extend(map(int, line.split()))
PRIMES_SET = set(PRIMES)
MAX_PRIME = PRIMES[-1]


def is_prime(num) -> bool:
    return num in PRIMES_SET


def primes(end: int = None) -> Iterator[int]:
    if end is None:
        return iter(PRIMES)
    else:
        return itertools.islice(iter(PRIMES), end)


def prime_factors(num) -> list:
    assert num <= PRIMES[-1], f'num {num} out of range'

    tmp = num
    factor_list = [1]
    for p in primes(end=int(num**.5+1)):
        while tmp % p == 0:
            factor_list.append(p)
            tmp //= p
        if tmp == 1:
            return factor_list

    return factor_list

