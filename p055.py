from utils.decorators import *


START_LIMIT = 10000
ITER_LIMIT = 50


cache = {}

def is_palindrome(num) -> bool:
    if not isinstance(num, str):
        num = str(num)

    for i in range(1, len(num) // 2 + 1):
        if num[i-1] != num[-i]:
            return False

    return True


def is_lychrel(num, iter_count = 1) -> bool:
    if num in cache:
        return cache[num]

    if iter_count == ITER_LIMIT:
        cache[num] = True
    else:
        sum = num + int(str(num)[::-1])

        if is_palindrome(sum):
            cache[num] = False
        else:
            cache[num] = is_lychrel(sum, iter_count + 1)

    return cache[num]


if __name__ == '__main__':
    print(len(list(filter(is_lychrel, range(1, START_LIMIT)))))
