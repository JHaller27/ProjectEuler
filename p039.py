import math


def is_int(f):
    return math.ceil(f) == math.floor(f)


def calc_a(b, P):
    return P * (P - 2 * b) / (2 * (P - b))


def check(b, P):
    a = calc_a(b, P)
    return is_int(a)


def count_solutions(P):
    return len(list(filter(lambda b: check(b, P), range(1, P // 2)))) // 2


def main():
    return max(range(3, 1001), key=count_solutions)


if __name__ == "__main__":
    ans = main()
    print(ans)
