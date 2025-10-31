"""
Author: Mohammed Umar
Description: This file depicts the working of a Doubly Linked List.
Date: 2025-10-31
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.size: int = 0

    def is_empty(self):
        return True if self.size == 0 else False

    def insert_first(self, value: Node) -> None:

        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            new_node.prev = self.head
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        return

    def insert(self, value: Node, pos: int = 0) -> None:

        if pos == 0:
            return self.insert_first(value)
