def bfs(root, fn):
    q = list()
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)
        fn(node)
        for child in node.get_children():
            q.append(child)
