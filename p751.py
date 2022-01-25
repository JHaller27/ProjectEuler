from math import floor
from functools import cache
from itertools import count


# theta = 2.956938891377988...
# sequence = 2, 3, 5, 8, 13, 21, 34, 55, 89, ... (fibo)
# tau = 2.3581321345589


@cache
def b(n: int, n_1: float) -> float:
    if n == 1:
        return n_1

    assert n >= 2, f"{n=}"

    bn1 = b(n-1, n_1)
    fbn1 = floor(bn1)

    return fbn1*(bn1-fbn1+1)


@cache
def a(n: int, n_1: float) -> int:
    return floor(b(n, n_1))


def tau(theta: float, places: int) -> str:
    total = ""
    for i in count(1):
        a_i = a(i, theta)
        # print(f"{a_i=}")
        total += str(a_i)
        if len(total) >= places + 1:
            break
    return total[0] + "." + total[1:places]


def find_match(theta: float):
    tau_val = tau(theta, 24)
    # while tau_val != str(theta):


def main(pow):
    # From these tests, we now know that roughly 10% of increasing theta values result in an increased tau value
    # Thus, we cannot perform a true binary search, but we can do a binary search w/ prioritization (instead of pruning)
    theta = 2.0
    delta = 10**(-pow)

    last_tau = tau(theta, 24)
    theta += delta

    total = 0
    breaks = 0

    while theta < 3:
        tau_val = tau(theta, 24)
        total += 1

        if tau_val < last_tau:
            breaks += 1

        last_tau = tau_val

        theta += delta

    return f"{(breaks * 100 / total)}%"


if __name__ == "__main__":
    import sys
    pow = int(sys.argv[1])
    ans = main(pow)
    print(ans)
