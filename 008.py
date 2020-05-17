from functools import reduce


def product(iterable) -> int:
    return reduce(lambda acc, e: acc * e, iterable)


if __name__ == '__main__':
    seq = []
    with open('data/008.txt', 'r') as fin:
        for line in fin:
            seq.extend(map(lambda d: int(d), line.strip()))

    max_product = 0
    size = 13
    for i in range(len(seq) - size):
        sub_seq = seq[i:i+size]
        if 0 not in sub_seq:
            max_product = max(max_product, product(sub_seq))

    print(max_product)
