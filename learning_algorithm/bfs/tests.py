import unittest

from bfs.bfs import bfs


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


class BFSTest(unittest.TestCase):
    def test_bfs_using_binary_tree(self):
        root = Node('root')
        node_1 = Node('node_1')
        node_2 = Node('node_2')
        node_3 = Node('node_3')
        node_4 = Node('node_4')
        node_5 = Node('node_5')
        node_6 = Node('node_6')
        node_7 = Node('node_7')
        node_8 = Node('node_8')

        #          root
        #         /    \
        #        1      2
        #       / \    / \
        #      3   4  5   6
        #     / \
        #    7   8

        root.left = node_1
        root.right = node_2
        node_1.left = node_3
        node_1.right = node_4
        node_2.left = node_5
        node_2.right = node_6
        node_3.left = node_7
        node_3.right = node_8

        output = []

        def fn(node):
            output.append(node.val)

        bfs(root, fn)
        self.assertEqual(['root', 'node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'node_7', 'node_8'],
                         output)
