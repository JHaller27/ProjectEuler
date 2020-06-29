class _CommentedFileIter:
    def __init__(self, fp):
        self._fitr = iter(fp)

    def __next__(self):
        while line := next(self._fitr):
            if line.startswith('#'):
                continue

            if "#" in line:
                comment_idx = line.index('#')
                line = line[:comment_idx]

            return line.rstrip()


class CommentedFile:
    def __init__(self, fname):
        self._fname = fname
        self._fp = open(self._fname, 'r')

    def close(self):
        self._fp.close()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def __iter__(self):
        return _CommentedFileIter(self._fp)


if __name__ == '__main__':
    fname = 'data/054_example.txt'

    with CommentedFile(fname) as fin:
        for line in fin:
            print(f'"{line}"')
