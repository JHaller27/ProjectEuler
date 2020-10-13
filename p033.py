import fractions


def main():
    # Given arbitrary fraction n/d, let
    #   n = 10 * n1 + n0
    #   d = 10 * d1 + d0
    # eg: given n/d = 49/98
    #   n1 = 4, n0 = 9
    #   d1 = 9, d0 = 8

    cum_n = 1
    cum_d = 1
    for d in range(10, 100):
        d1, d0 = d // 10, d % 10

        for n in range(10, d):
            n1, n0 = n // 10, n % 10

            # Check if n0/d1 == n/d (via cross-product), or
            #          n1/d0 == n/d (via cross-product)
            if (n1 == d0 and n0 * d == d1 * n) or (n0 == d1 and n1 * d == d0 * n):
                cum_n *= n
                cum_d *= d

    return cum_d // fractions.gcd(cum_n, cum_d)


if __name__ == "__main__":
    ans = main()
    print(ans)
