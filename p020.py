from functools import reduce

print(sum(map(int, str(reduce(lambda acc, e: acc * e, range(2, 101), 1)))))
