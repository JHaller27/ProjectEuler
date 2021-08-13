from functools import cache


@cache
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    return a * pow(a, b-1)


def get_digital_sum(n):
    return sum(map(int, str(n)))


def get_pows():
    for a in range(100):
        for b in range(100):
            yield pow(a, b)


pow_itr = get_pows()
digital_sum_itr = map(get_digital_sum, pow_itr)
max_sum = max(digital_sum_itr)
print(max_sum)
