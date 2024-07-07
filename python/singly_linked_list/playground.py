class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        current_head = self.head
        penultimate_head = current_head
        print(penultimate_head.value)
        while current_head.next != None:
            penultimate_head = current_head
            current_head = current_head.next
        self.tail = penultimate_head
        self.tail.next = None
        self.length -= 1
        return current_head.value

    def shift(self):
        if not self.head:
            return None
        old_head = self.head
        self.head = old_head.next # Make second node the head
        old_head.next = None # Set old head node's next to None

        self.length -= 1
        return old_head.value

    def unshift(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return self

    

if __name__ == "__main__":

    sll = SinglyLinkedList()
    print(sll.head)
    print(sll.tail)
    sll.unshift("Mohan")
    sll.unshift("Badhreesh")
    print(sll.head.value, sll.head.next.value)
    print(sll.tail.value, sll.tail.next)
    
