from collections import defaultdict
from stack.stack import Stack


def dfs_recursion(root, fn):
    visited = defaultdict(bool)
    visited[root] = True
    fn(root)
    for child in root.get_children():
        if not visited.get(child):
            dfs_recursion(child, fn)


def dfs_stack(root, fn):
    stack = Stack()
    stack.push(root)
    visited = defaultdict(bool)
    visited[root] = True
    fn(root)

    while not stack.is_empty():
        node = stack.get_top()
        for child in node.get_children():
            if not visited.get(child):
                fn(child)
                visited[child] = True
                stack.push(child)
            else:
                stack.pop()
