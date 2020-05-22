import itertools


LIMIT = 28123


def main():
    sum_of_divisors = [0] * LIMIT
    for i in range(1, len(sum_of_divisors)):
        for j in range(i * 2, LIMIT, i):
            sum_of_divisors[j] += i

    abundant_nums = [num for num, sod in enumerate(sum_of_divisors) if sod > num]

    sum_of_abundants = [False] * len(sum_of_divisors)
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j < len(sum_of_abundants):
                sum_of_abundants[i + j] = True
            else:
                break

    return sum(itertools.compress(range(LIMIT), map(lambda b: not b, sum_of_abundants)))


if __name__ == '__main__':
    ans = main()
    print(ans)
