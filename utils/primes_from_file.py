from typing import Iterator
import itertools

PRIMES = []

with open('./data/primes.txt', 'r') as fin:
    for line in fin:
        PRIMES.extend(map(int, line.split()))
PRIMES_SET = set(PRIMES)


def is_prime(num) -> bool:
    return num in PRIMES_SET


def primes(start: int = None, end: int = None, count: int = None) -> Iterator[int]:
    start_idx = 0 if start is None else PRIMES.index(start)

    assert count is not None and count-start_idx <= len(PRIMES), f'count must not be greater than {len(PRIMES)}'
    assert end is not None and end <= PRIMES[-1], f'end {end} out of range'

    sliced_primes = PRIMES[start_idx:count]

    return sliced_primes if end is None else itertools.takewhile(lambda p: p < end, sliced_primes)


def prime_factors(num) -> list:
    assert num <= PRIMES[-1], f'num {num} out of range'

    tmp = num
    factor_list = [1]
    for p in primes(end=num**.5+1):
        while tmp % p == 0:
            factor_list.append(p)
            tmp //= p
        if tmp == 1:
            return factor_list

    return factor_list

