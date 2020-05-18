MAX_A = 999
MAX_B = 1000

sieve = [False, False, True, True]
def is_prime(num):
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


def count_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n


max_coef = 0
max_count = 0
for a in range(-MAX_A, MAX_A):
    for b in range(-MAX_B, MAX_B):
        if (count := count_primes(a, b)) > max_count:
            max_count = count
            max_coef = a * b

print(max_coef)
