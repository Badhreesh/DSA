from sll import SinglyLinkedList

def main():
    sll = SinglyLinkedList()

    sll.push("Badhreesh")
    sll.push("Mohan")
    sll.push("Rao")

    print(sll.length)
    sll.traverse()
    print()

    while True:
        try:
            sll.pop()
            print(sll.length)
            sll.traverse()
            print()
        except AttributeError:
            print(f"Linked list is empty ({sll.length=}). Cannot pop further.")
            break


if __name__ == "__main__":
    main()
