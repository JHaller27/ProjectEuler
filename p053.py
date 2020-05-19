import math

def C(n, r):
    assert r <= n

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def get_n_r(n_max):
    for n in range(1, n_max+1):
        for r in range(1, n+1):
            yield n, r

print(len(list(filter(lambda v: v > 10**6, [C(n, r) for n, r in get_n_r(100)]))))

