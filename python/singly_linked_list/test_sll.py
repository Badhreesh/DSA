from sll import Node, SinglyLinkedList

def test_push():
    """
    Test adding a node to the end of the sll.
    """
    sll = SinglyLinkedList()
    assert sll.length == 0

    sll.push("Badhreesh")
    sll.push("Mohan")
    sll.push("Rao")
    
    assert sll.head and sll.tail is not None

    assert sll.head.value == "Badhreesh"
    assert isinstance(sll.head.next, Node)

    assert sll.tail.value == "Rao"
    assert sll.tail.next == None

    assert sll.length == 3

def test_pop():
    """
    Test removing a node from the end of the sll.
    """
    sll = SinglyLinkedList()

    sll.push("Badhreesh")
    sll.push("Mohan")
    sll.push("Rao")

    assert sll.tail is not None
    assert sll.tail.value == "Rao"
    assert sll.length == 3

    sll.pop()

    assert sll.tail is not None
    assert sll.tail.value == "Mohan"
    assert sll.length == 2

def test_shift():
    """
    Test removing a node from the beginning of the sll.
    """
    sll = SinglyLinkedList()

    sll.push("Badhreesh")
    sll.push("Mohan")
    sll.push("Rao")

    assert sll.head and sll.tail is not None
    assert sll.head.value == "Badhreesh"
    assert isinstance(sll.head.next, Node)

    assert sll.length == 3

    sll.shift()

    assert sll.head and sll.tail is not None
    assert sll.head.value == "Mohan"
    assert sll.length == 2

def test_unshift():
    """
    Test adding a node to the beginning of the sll.
    """
    sll = SinglyLinkedList()

    sll.push("Mohan")
    sll.push("Rao")

    assert sll.head is not None
    assert sll.head.value == "Mohan"
    assert sll.length == 2

    sll.unshift("Badhreesh")

    assert sll.head is not None
    assert sll.head.value == "Badhreesh"
    assert isinstance(sll.head.next, Node)
    assert sll.length == 3

def test_get():
    sll = SinglyLinkedList()

    sll.push("Mohan")
    sll.push("Rao")

    assert sll.head is not None
    assert sll.head.value == "Mohan"
    assert sll.length == 2

    node = sll.get(position=1)
    assert isinstance(node, Node)
    assert node.value == "Rao"

    node = sll.get(position=10)
    assert node is None

# def test_pop_empty_sll():
#     sll = SinglyLinkedList()
#     with pytest.raises(AttributeError) as exc_info:
#         sll.pop()
#         print(exc_info.type)

