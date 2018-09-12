def in_order_traversal(root):
    tree = []
    current = root
    done = False
    stack = []

    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                tree.append(current)
                current = current.right
            else:
                done = True
