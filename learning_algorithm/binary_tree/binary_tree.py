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


def pre_order(root):
    res = []
    if root is None:
        return []
    res.append(root.val)
    res.extend(pre_order(root.left))
    res.extend(pre_order(root.right))
    return res


def in_order(root):
    res = []
    if root is None:
        return []
    res.extend(in_order(root.left))
    res.append(root.val)
    res.extend(in_order(root.right))
    return res


def post_order(root):
    res = []
    if root is None:
        return []
    res.extend(post_order(root.left))
    res.extend(post_order(root.right))
    res.append(root.val)
    return res


def level_order(root):
    if root is None:
        return []

    res = []
    q = [root]

    while q:
        q1 = []
        level = []
        for node in q:
            level.append(node.val)
            if node.left is not None:
                q1.append(node.left)
            if node.right is not None:
                q1.append(node.right)
            q = q1
        res.append(level)
    return res
