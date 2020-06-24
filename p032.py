def main():
    # We only need to check products 1-10,000
    # Consider the equation x * y = z.
    # We define a "pandigital product" as a product where the digits of x, y, and z contain all 9 digits 1-9 exactly once each.
    # If the product z contains 5+ digits (z >= 10000), then the operands x and y must contain 4 digits between them.
    # The greatest possible z given 4 digits shared between x and y is 99 * 99 which is <10000.
    # Thus, there is no possible pandigital product >=10000.
    return sum(filter(is_pandigital_product, range(1, 10000)))


def is_pandigital_product(product):
    DIGITS = '123456789'

    # For each candidate factor 2 - sqrt(product)...
    # We ignore candidate factor 1 given that 1 * y = y, which clearly cannot be pandigital
    for candidate in range(2, int(product**0.5)):
        # If this candidate is indeed a factor...
        if product % candidate == 0:
            # Return true iff the digits contain all digits 1-9 exactly once
            digits = ''.join(sorted(str(product) + str(candidate) + str(product // candidate)))
            if digits == DIGITS:
                return True

    return False


if __name__ == '__main__':
    ans = main()
    print(ans)
