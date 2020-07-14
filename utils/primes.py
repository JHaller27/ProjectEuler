from typing import Iterator
import utils.primes_from_file as pfile
import itertools


def is_prime(num) -> bool:
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0:
        return False

    if num < pfile.MAX_PRIME:
        return pfile.is_prime(num)

    for mod in range(3, int(num**0.5)+1, 2):
        if num % mod == 0:
            return False

    return True


def primes(end: int) -> Iterator[int]:
    if end < 2:
        return

    sieve = [True] * end
    sieve_end = int(end ** 0.5)

    for p in itertools.takewhile(lambda p: p < end, pfile.primes()):
        yield p

        if p <= sieve_end:
            for mult in range(p*2, len(sieve), p):
                sieve[mult] = False


    # Sieve of Eratosthenes
    for p in range(pfile.MAX_PRIME, len(sieve)):
        if sieve[p]:
            yield p
            if p <= sieve_end:
                for mult in range(p*2, len(sieve), p):
                    sieve[mult] = False


def prime_factors(num) -> list:
    try:
        return pfile.prime_factors(num)
    except AssertionError:
        tmp = num
        factor_list = [1]
        for p in primes(end=num ** .5 + 1):
            while tmp % p == 0:
                factor_list.append(p)
                tmp //= p
            if tmp == 1:
                return factor_list

        return factor_list
