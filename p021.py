from utils.decorators import *


@memoize()
def d(n):
    return sum(x for x in range(1, n) if n % x == 0)


print(sum(n for n in range(10000) if d(n) != n and d(d(n)) == n))
