from utils.decorators import *


@memoize()
def is_palindrome(num: str) -> bool:
    if len(num) <= 1:
        return True

    if len(num) == 2:
        return num[0] == num[1]

    if num[0] != num[-1]:
        return False

    return is_palindrome(num[1:-1])


def palindromes(len_limit: int, start = '') -> list:
    pals = []
    for i in range(10):
        pal = f'{i}{start}{i}'
        if pal[0] != '0':
            pals.append(pal)
        if len(pal) + 2 <= len_limit:
            pals.extend(palindromes(len_limit, pal))
    return pals


def bin_is_palindrome(num: int):
    return is_palindrome(bin(int(num))[2:])


if __name__ == '__main__':
    LIMIT = len(str(10**6)) - 1
    pals = palindromes(LIMIT, '')
    for i in range(10):
        pals.append(i)
        pals.extend(palindromes(LIMIT, str(i)))

    l = set(map(int, filter(bin_is_palindrome, pals)))

    for e in l:
        print(f'{e} -> {bin(int(e))[2:]}')

    print(sum(map(int, l)))
