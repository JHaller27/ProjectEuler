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


def main():
    for a in range(100, 1000):
        for b in range(100, 1000):
            if is_palindrome(str(a*b)):
                yield a * b


if __name__ == '__main__':
    print(max(main()))
