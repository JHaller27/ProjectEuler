from utils.decorators import *


@memoize()
def get_triangle_num(num: int) -> int:
    if num == 1:
        return 1

    return num + get_triangle_num(num-1)


def count_factors(num: int) -> int:
    if num == 1:
        return 1

    return 2*len([i for i in range(1, int(num**.5)+1) if num % i == 0])


if __name__ == "__main__":
    COUNT_LIMIT = 500
    n = 1
    while count_factors(get_triangle_num(n)) < COUNT_LIMIT:
        n += 1
    print(get_triangle_num(n))
