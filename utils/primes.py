import utils.sieve_of_eratosthenes as sieve
import utils.primes_from_file as pfile


sieve.is_prime(pfile.PRIMES[-1])

def is_prime(num) -> bool:
    try:
        return pfile.is_prime(num)
    except AssertionError:
        return sieve.is_prime(num)


def primes(start: int = 2, end: int = None, count: int = None) -> int:
    try:
        return pfile.primes(start, end, count)
    except AssertionError:
        sieve.is_prime(end)

        return sieve.primes(start, end, count)


def prime_factors(num) -> list:
    try:
        return pfile.prime_factors(num)
    except AssertionError:
        return sieve.prime_factors(num)
