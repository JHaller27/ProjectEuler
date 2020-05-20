import itertools

LIMIT = 10**6-1
print(list(itertools.islice(map(lambda e: ''.join(e), itertools.permutations('0123456789')), LIMIT, LIMIT+1))[0])

