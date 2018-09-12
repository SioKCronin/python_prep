class Node(object):
    def __init__(self):
        self.next = None
        self.value = None

one = Node()
two = Node()
three = Node()

x = one
one.next = two
two.next = three
three.next = one

one.value = 1

print(x.value)
