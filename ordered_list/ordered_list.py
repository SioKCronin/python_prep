from unordered_list import Node, UnorderedList

class OrderedList(UnorderedList):

    def search(self, item):
        current = self.head

        while urrent is not None:
            if current_value == item:
                return True
            if current.value > item:
                return False
            current = current.next

        return False

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        temp = Node(item)
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
