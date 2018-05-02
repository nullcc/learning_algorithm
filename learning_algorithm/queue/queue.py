class Queue:
    def __init__(self):
        self._queue = []
        self._cur_idx = -1

    def enqueue(self, element):
        self._queue.append(element)

    def dequeue(self):
        return self._queue.pop(0)

    def is_empty(self) -> int:
        return len(self._queue) == 0

    def size(self) -> int:
        return len(self._queue)

    def __iter__(self):
        return self

    def __next__(self):
        self._cur_idx += 1
        if self._cur_idx >= len(self._queue):
            raise StopIteration
        element = self._queue[self._cur_idx]
        return element
