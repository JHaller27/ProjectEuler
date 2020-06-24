def main():
    current_max = 0

    # We only need to check for num < 10000. Proof follows.
    # We define "pandigital equation" as an equation of the form
    # x * y = z_y where y varies >= 1 the digits of z_y (all y >= 1, but y < some limit > 1) contain each digit 1-9 exactly once.
    # If x >= 10000 (which contains 5 digits), then z_1 = x * 1 = x >= 10000. Thus, z_1 contains 5 digits and cannot itself be pandigital.
    # So we continue: z_2 = x * 2 >= 20000. Thus, z_1 concatenated with z_2 contains at least 10 digits, which is not pandigital.
    # z_y where y > 2 clearly only produces concatenations of more digits, and can never be pandigital.
    for num in range(1, 10000):
        if pandigital := get_pandigital_multiples(num):
            current_max = pandigital

    return current_max


def get_pandigital_multiples(num):
    DIGITS = '123456789'
    digits = ''

    mult = num
    while len(digits) < 9:
        digits += str(mult)
        mult += num

    if ''.join(sorted(digits)) == DIGITS:
        return digits


if __name__ == '__main__':
    ans = main()
    print(ans)
