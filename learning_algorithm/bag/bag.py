class Bag:
    def __init__(self):
        self._bag = []
        self._cur_idx = -1

    def add(self, element):
        self._bag.append(element)

    def is_empty(self) -> int:
        return len(self._bag) == 0

    def size(self) -> int:
        return len(self._bag)

    def __iter__(self):
        self._cur_idx = -1
        return self

    def __next__(self):
        self._cur_idx += 1
        if self._cur_idx >= len(self._bag):
            raise StopIteration
        element = self._bag[self._cur_idx]
        return element
