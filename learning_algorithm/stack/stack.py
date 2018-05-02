class Stack:
    def __init__(self):
        self._stack = []
        self._cur_idx = -1

    def push(self, element):
        self._stack.insert(0, element)

    def pop(self):
        return self._stack.pop(0)

    def is_empty(self) -> int:
        return len(self._stack) == 0

    def size(self) -> int:
        return len(self._stack)

    def __iter__(self):
        self._cur_idx = -1
        return self

    def __next__(self):
        self._cur_idx += 1
        if self._cur_idx >= len(self._stack):
            raise StopIteration
        element = self._stack[self._cur_idx]
        return element
