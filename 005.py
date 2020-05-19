import utils.sieve_of_eratosthenes as sieve
from functools import reduce


MULT_LIMIT = 20

all_factors = {}
for i in range(2, MULT_LIMIT+1):
    factors = sieve.prime_factors(i)
    d = {i: 1} if sieve.is_prime(i) else {}
    for f in factors:
        if f is not 1:
            if f not in d:
                d[f] = 1
            else:
                d[f] += 1

    for f in d:
        if f not in all_factors:
            all_factors[f] = d[f]
        elif all_factors[f] < d[f]:
            all_factors[f] = d[f]


print(reduce(lambda acc, k: acc * k**all_factors[k], all_factors, 1))
