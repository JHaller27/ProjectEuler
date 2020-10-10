import itertools
import utils.primes as primes


def main():
    prime_count = 0
    total_count = 1
    num = 1

    for side_length in itertools.count(3, 2):
        for _ in range(4):
            total_count += 1

            num += side_length - 1

            if primes.is_prime(num):
                prime_count += 1

            if prime_count / total_count < .1:
                return side_length

if __name__ == "__main__":
    ans = main()
    print(ans)
