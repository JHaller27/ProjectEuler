sieve = [False, False, True, True]
def is_prime(num) -> bool:
    if num < len(sieve):
        if 0 <= num:
            return sieve[num]
        return False

    # Extend
    old_end = len(sieve)
    sieve.extend([True] * (num - len(sieve) + 1))
    for p in range(2, old_end):
        if sieve[p]:
            mult = 2
            while p * mult < len(sieve):
                sieve[p * mult] = False
                mult += 1

    return sieve[num]


def primes(start: int = 2, end: int = None, count: int = None) -> int:
    yielded = 0
    while (end is None or start < end) and (count is None or yielded < count):
        if is_prime(start):
            yielded += 1
            yield start
        start += 1


def factors(num) -> list:
    tmp = num
    factor_list = [1]
    for p in primes(end=num**.5):
        while tmp % p == 0:
            factor_list.append(p)
            tmp //= p
        if tmp == 1:
            return factor_list

    return factor_list
