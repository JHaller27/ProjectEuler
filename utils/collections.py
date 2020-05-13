import heapq

class Collection:
    def __init__(self, init = None):
        self._lst = [] if init is None else init

    def __len__(self) -> int:
        return len(self._lst)

    def __str__(self) -> str:
        return str(self._lst)

    def __next__(self):
        if len(self) == 0:
            raise StopIteration()

        return self.pop()

    def __iter__(self):
        return self.copy()

    def copy(self) -> 'Collection':
        return self.__class__(self._lst.copy())

    def clear(self):
        self._lst = []

    def push_many(self, items):
        for el in items:
            self.push(el)

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


class MinHeap(Collection):
    def __init__(self, init = None):
        heapq.heapify(init)
        super().__init__(init)

    def push(self, item):
        heapq.heappush(self._lst, item)

    def pop(self):
        return heapq.heappop(self._lst)

    def peek(self, idx = 0):
        return self._lst[idx]


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

    # Queue iterator
    q = Queue([1, 2, 3])

    assert len(q) == 3

    i = 1
    for el in q:
        expect('Queue:next', el, i)
        i += 1

    expect('Queue:len after iteratation', len(q), 3)

    # Compare performance of list / heap
    import time
    import random

    l = [i for i in range(10000)]
    random.shuffle(l)

    # list
    times = 0
    count = 0
    for _ in range(10):
        l1 = l.copy()
        start = time.perf_counter()
        llen = len(l)
        for i in range(llen):
            x = min(l1)
            l1.remove(x)
            assert x == i
        end = time.perf_counter()
        times += end - start
        count += 1
    avg_list_time = times / count

    # heap
    times = 0
    count = 0
    for _ in range(10):
        l1 = MinHeap(l.copy())
        start = time.perf_counter()
        llen = len(l)
        for i in range(llen):
            x = l1.pop()
            assert x == i
        end = time.perf_counter()
        times += end - start
        count += 1
    avg_heap_time = times / count

    if avg_heap_time >= avg_list_time:
        print('Expected min heap to be faster than flat lists')
        print(f'\tHeap avg time: {avg_heap_time} sec')
        print(f'\tList avg time: {avg_list_time} sec')
