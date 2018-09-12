# Tree Traversal

## In-order
```
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
```
## Pre-order
```
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
```
## Post-order

```
def postorder(root):
    tree = []
    current = root
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    return reversed(s2)
```

## Spanning tree
