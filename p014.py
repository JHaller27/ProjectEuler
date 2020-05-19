import sys
from utils.decorators import *

sys.setrecursionlimit(10**6)


@memoize()
def length(n) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + length(n // 2)
    return 1 + length(3 * n + 1)


print(max(range(1, 10**6), key=length))
