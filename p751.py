import math


PRECISION = 15


def seq(theta: int):
    theta = 2 + theta / (10**PRECISION)

    # yield math.floor(theta)

    digits = 0

    b_last = theta
    while True:
        b_last_int = math.floor(b_last)
        b = b_last_int * (b_last - b_last_int + 1)
        b_int = math.floor(b)
        yield b_int

        digits += math.ceil(math.log10(b_int))
        if digits >= PRECISION:
            return

        b_last = b


def check(theta: int) -> int:
    for a in seq(theta):
        theta_len = math.ceil(math.log10(theta))
        a_len = math.ceil(math.log10(a))
        rem_len = theta_len - a_len

        theta_base, theta = divmod(theta, 10**rem_len)

        diff = theta_base - a
        if diff != 0:
            return diff

    return 0


def main():
    theta = 5 * 10**PRECISION

    c = check(theta)
    while True:
        if c == 0:
            return float(f'2.{theta}')

        if c < 0:
            # TODO Lower by half
            pass
        else:
            # TODO Raise by half
            pass


if __name__ == "__main__":
    ans = main()
    print(ans)
