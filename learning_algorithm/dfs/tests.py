import unittest

from dfs.dfs import dfs_recursion


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


class DFSTest(unittest.TestCase):
    def test_dfs_recursion_using_binary_tree(self):
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

        dfs_recursion(root, fn)
        self.assertEqual(['root', 'node_1', 'node_3', 'node_7', 'node_8', 'node_4', 'node_2', 'node_5', 'node_6'],
                         output)

    def test_dfs_stack_using_binary_tree(self):
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

        dfs_recursion(root, fn)
        self.assertEqual(['root', 'node_1', 'node_3', 'node_7', 'node_8', 'node_4', 'node_2', 'node_5', 'node_6'],
                         output)
