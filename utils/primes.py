from typing import Iterator
import utils.primes_from_file as pfile


def is_prime(num) -> bool:
    if num < pfile.PRIMES[-1]:
        return pfile.is_prime(num)
    else:
        if num % 2 == 0:
            return False

        for mod in range(3, int(num**0.5)+1, 2):
            if num % mod == 0:
                return False

        return True


def primes(start: int = 2, end: int = None, count: int = None) -> Iterator[int]:
    try:
        return pfile.primes(start, end, count)
    except AssertionError:
        yielded = 0
        while (end is None or start < end) and (count is None or yielded < count):
            if is_prime(start):
                yielded += 1
                yield start
            start += 1


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
