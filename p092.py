MEMOIZED = {1: 1, 89: 89}

def square_digits(num: int):
    total = 0
    while num > 0:
        total += (num % 10)**2
        num //= 10
    return total


def sq_dig_chain(x):
    new_digs = set([x])

    while x != 1 and x != 89 and x not in MEMOIZED:
        new_digs.add(x)
        x = square_digits(x)

    for k in new_digs:
        MEMOIZED[k] = MEMOIZED[x]

    return MEMOIZED[x]


def main():
    END = 10*10**6
    # END = 100
    return len(list(filter(lambda x: sq_dig_chain(x) == 89, range(2, END))))


if __name__ == '__main__':
    ans = main()
    print(ans)
