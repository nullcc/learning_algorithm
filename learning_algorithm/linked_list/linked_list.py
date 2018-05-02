class LinkedList:

    class Node:
        def __init__(self, item, next_node=None):
            self.item = item
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def add(self, element):
        self.add_last(element)

    def add_first(self, element):
        if self.head is None:
            self.add_last(element)
        else:
            new_node = self.Node(element, None)
            new_node.next_node = self.head
            self.head = new_node
            self.node_count += 1

    def add_last(self, element):
        if self.head is None:
            self.head = self.Node(element, None)
            self.tail = self.head
        else:
            new_node = self.Node(element, None)
            self.tail.next_node = new_node
            self.tail = new_node
        self.node_count += 1

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def size(self):
        return self.node_count

    def __iter__(self):
        self._cur_node = self.head
        return self

    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        node = self._cur_node
        self._cur_node = self._cur_node.next_node
        return node

    def get_index(self, index):
        if 0 < index < self.size():
            cur_index = 0
            cur_node = self.head
            node = cur_node
            while cur_index != index:
                cur_node = cur_node.next_node
                cur_index += 1
                node = cur_node
            return node
