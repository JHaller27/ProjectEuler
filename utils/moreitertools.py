import itertools


def itake(iterable, idx: int):
    return next(itertools.islice(iterable, idx, idx+1))
