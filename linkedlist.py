class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def _check_index_bound(self, pos: int):
        if pos > self.size:
            raise Exception("Index out of Bounds")

    def is_empty(self) -> bool:
        return True if self.size == 0 else False

    def print_ll(self):
        head_node = self.head

        for i in range(self.size):
            print(head_node.data)
            head_node = head_node.next

    def seek_value(self, value: int) -> Node:

        head_node = self.head

        for i in range(self.size):

            if head_node.data != value:
                prev_node = head_node
                head_node = head_node.next
            elif head_node.data == value:
                return prev_node if prev_node else head_node

            else:
                raise Exception("Value not Found")

    def seek(self, pos: int) -> Node:

        self._check_index_bound(pos)

        if pos == 0:
            return self.head

        head_node = self.head
        i = 0
        while i < pos - 1:
            head_node = head_node.next

            i += 1
        return head_node

    def insert_first(self, value: int) -> None:

        new_node = Node(value)

        if self.is_empty():
            print(f"Linkedlist is empty, inserting value: {value}")
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node

        self.size += 1

        return

    def insert(self, value: int, pos: int = 0) -> None:

        self._check_index_bound(pos)

        if pos == 0 or self.is_empty():
            self.insert_first(value)
            return

        new_node = Node(value)

        head_at_pos = self.seek(pos)

        new_node.next = head_at_pos.next
        head_at_pos.next = new_node
        self.size += 1
        return

    def delete(self, value: int) -> None:

        prev_node = self.seek_value(value)

        prev_node.next = prev_node.next.next
        self.size -= 1
        return

    def delete_pos(self, pos: int = 0) -> None:

        if self.is_empty():
            raise Exception("List is Empty")

        if pos == 0:
            self.head = self.head.next
            self.size -= 1
            return

        prev_node = self.seek(pos)
        prev_node.next = prev_node.next.next
        self.size -= 1
        return

    def reverse(self) -> None:

        current = self.head
        prev: Node = None

        i = 0

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

            i = i + 1

        self.head = prev


ll = LinkedList()

ll.insert(5)
ll.insert(2)
ll.insert(7)
ll.print_ll()
print("#" * 30)
# ll.insert(9, 2)
# ll.insert(11, 3)
# ll.print_ll()
print("Size after all insertions:", ll.size)


ll.reverse()
print("Head is at:", ll.head.data)
ll.print_ll()
# ll.delete(11)
# ll.delete_pos(2)
# print("Size after deletion", ll.size)
# ll.print_ll()
