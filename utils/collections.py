class Collection:
    def __init__(self, init = None):
        self._lst = [] if init is None else init

    def __len__(self) -> int:
        return len(self._lst)

    def __str__(self) -> str:
        return str(self._lst)

    def copy(self) -> 'Collection':
        return self.__class__(self._lst.copy())

    def clear(self):
        self._lst = []

    def push(self, item):
        raise NotImplementedError('Method not implemented')

    def pop(self):
        raise NotImplementedError('Method not implemented')

    def peek(self, idx = None):
        raise NotImplementedError('Method not implemented')


class Stack(Collection):
    def push(self, item):
        self._lst.append(item)

    def pop(self):
        return self._lst.pop()

    def peek(self, idx = None):
        return self._lst[-1]


class Queue(Collection):
    def push(self, item):
        self._lst.append(item)

    def pop(self):
        return self._lst.pop(0)

    def peek(self, idx = None):
        return self._lst[0]


if __name__ == '__main__':
    def expect(title: str, actual, expected):
        if actual != expected:
            print(f'{title} expected {actual} == {expected}')

    print('Testing collections...')

    # Stack push/pop/peek/len
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    expect('Stack:len after push', len(s), 3)

    expect('Stack:peek', s.peek(), 3)
    expect('Stack:peek', s.peek(), 3)

    expect('Stack:pop', s.pop(), 3)
    expect('Stack:pop', s.pop(), 2)
    expect('Stack:pop', s.pop(), 1)

    expect('Stack:len after pop', len(s), 0)

    # Stack copy/clear
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    sp = s.copy()

    s.pop()
    expect('Stack copy', sp.peek(), 3)

    assert len(s) > 0
    s.clear()
    expect('Stack:len after clear', len(s), 0)

    # Queue push/pop/peek/len
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    expect('Queue:len after push', len(q), 3)

    expect('Queue:peek', q.peek(), 1)
    expect('Queue:peek', q.peek(), 1)

    expect('Queue:pop', q.pop(), 1)
    expect('Queue:pop', q.pop(), 2)
    expect('Queue:pop', q.pop(), 3)

    expect('Queue:len after pop', len(q), 0)

    # Queue copy/clear
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    sp = q.copy()

    q.pop()
    expect('Queue copy', sp.peek(), 1)

    assert len(q) > 0
    q.clear()
    expect('Queue:len after clear', len(q), 0)
