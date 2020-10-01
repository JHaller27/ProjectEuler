import itertools


def get_cycle_length(d):
    digits = {}
    r = 1
    for i in itertools.count(1):
        if r in digits:
            return i - digits[r]
        digits[r] = i
        r = r * 10 % d

def main():
    return max(range(1, 1000), key=get_cycle_length)


if __name__ == "__main__":
    ans = main()
    print(ans)
