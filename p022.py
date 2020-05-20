with open('data/022.txt', 'r') as fin:
    print(sum((idx + 1) * sum(map(lambda c: ord(c) - ord('A') + 1, name))
        for idx, name in enumerate(sorted(fin.read().replace('"', '').split(',')))
    ))
