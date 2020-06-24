import itertools


def itake(iterable, idx: int):
    return next(itertools.islice(iterable, idx, idx+1))


def itake_many(iterable, idxs):
    sorted_idxs = sorted(idxs)
    ei = enumerate(iterable)

    while len(sorted_idxs) > 0:
        i, e = next(ei)
        if i == sorted_idxs[0]:
            yield e
            sorted_idxs.pop(0)
