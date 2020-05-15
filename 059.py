import re

ALPHABET = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

with open('data/059.txt', 'r') as fin:
    CIPHER_LIST = list(map(int, fin.readline().split(',')))


show_regex = re.compile(r'^[^\|\~\@\`]+$')


def shift(cipher, key) -> bool:
    s = ''.join([chr(num ^ (key[idx % len(key)])) for idx, num in enumerate(cipher)])

    if show_regex.match(s) is None:
        return False

    print(s)
    halt = input('Halt? [y/N]')
    print()

    return len(halt) == 0 or halt[0].lower() == 'y'


def find_shift() -> list:
    for a in ALPHABET:
        for b in ALPHABET:
            for c in ALPHABET:
                key = [a, b, c]
                halt = shift(CIPHER_LIST, key)
                if halt:
                    s = sum([num ^ (key[idx % len(key)]) for idx, num in enumerate(CIPHER_LIST)])
                    return s


if __name__ == '__main__':
    print(find_shift())
