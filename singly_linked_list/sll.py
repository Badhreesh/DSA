from typing import Any

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

class SinglyLinkedList:
    """
    Original sll implementation from course.
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def unshift(self, value) -> None:
        """
        Add a node to the beginning of the sll.
        """
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def push(self, value) -> None:
        """
        Add a node to the end of the sll.
        """
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1


    def traverse(self):
        """
        Walk through the sll and print the elements in it. Only used for sanity purposes.
        """
        current_node = self.head
        while current_node.next:
            print(current_node.value)
            current_node = current_node.next
        print(self.tail.value)

    def shift(self) -> None | Node:
        """
        Remove a node from the beginning of the sll.
        """
        if not self.head: return None
        current_node = self.head
        self.head = current_node.next
        self.length -= 1
        if self.length == 0:
            self.head, self.tail = None, None
        return current_node

    def pop(self) -> None | Node:
        """
        Remove a node from the end of the sll.
        """
        if not self.head: return None
        current_node = self.head
        penultimate_node = current_node
        while current_node.next:
            penultimate_node = current_node
            current_node = current_node.next
        self.tail = penultimate_node
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head, self.tail = None, None
        return current_node

    def get(self):
        """
        Retrieving a node by its position in the sll.
        """
        ...
