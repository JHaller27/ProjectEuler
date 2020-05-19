with open('data/013.txt', 'r') as fin:
    print(str(sum(map(int, [line.strip() for line in fin])))[:10])
