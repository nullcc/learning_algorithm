import unittest

from binary_tree.binary_tree import Node, pre_order, in_order, post_order, level_order


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.root = Node('root')
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

        self.root.left = node_1
        self.root.right = node_2
        node_1.left = node_3
        node_1.right = node_4
        node_2.left = node_5
        node_2.right = node_6
        node_3.left = node_7
        node_3.right = node_8

    def test_pre_order_binary_tree(self):
        res = pre_order(self.root)
        self.assertEqual(['root', 'node_1', 'node_3', 'node_7', 'node_8', 'node_4', 'node_2', 'node_5', 'node_6'],
                         res)

    def test_in_order_binary_tree(self):
        res = in_order(self.root)
        self.assertEqual(['node_7', 'node_3', 'node_8', 'node_1', 'node_4', 'root', 'node_5', 'node_2', 'node_6'],
                         res)

    def test_post_order_binary_tree(self):
        res = post_order(self.root)
        self.assertEqual(['node_7', 'node_8', 'node_3', 'node_4', 'node_1', 'node_5', 'node_6', 'node_2', 'root'],
                         res)

    def test_level_order_binary_tree(self):
        res = level_order(self.root)
        self.assertEqual([['root'], ['node_1', 'node_2'], ['node_3', 'node_4', 'node_5', 'node_6'], ['node_7', 'node_8']],
                         res)
