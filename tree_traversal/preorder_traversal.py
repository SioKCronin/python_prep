def preorder_traversal(root):
    tree = []
    stack = []
    current = root
    if not current: return
    s.append(root)
    while stack:
        current = stack.pop()
        tree.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
