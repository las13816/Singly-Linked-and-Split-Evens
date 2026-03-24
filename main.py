from singly_linked_list import SinglyLinkedList

def main():
    print("---- Build a forward list ----")
    sll = SinglyLinkedList()
    sll.build_list_forward([10, 20, 30, 40, 50])
    print(sll.display())

    sll.delete_first()
    print("Delete the first node:", sll.display())

    sll.delete_last()
    print("Delete the last node:", sll.display())

    sll.delete_value(30)
    print("Delete the interior node:", sll.display())

    print("---- Build a backward list ----")
    sll = SinglyLinkedList()
    sll.build_list_backward([10, 20, 30, 40, 50])
    print(sll.display())

    sll.delete_first()
    print("Delete the first node:", sll.display())

    sll.delete_last()
    print("Delete the last node:", sll.display())

    sll.delete_value(30)
    print("Delete the interior node:", sll.display())

    print("---- Non-recursive reverse print test----")
    sll = SinglyLinkedList()
    sll.build_list_forward([10, 20, 30, 40, 50])
    print("Insertion order:", sll.display())
    print("Reverse order (non-recursive):", sll.display_reverse_nr())

    print("---- Remove all test ----")
    sll = SinglyLinkedList()
    sll.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    print(sll.display())

    sll.remove_all(1)
    print("Removing 1 and all duplicates:", sll.display())

    sll.remove_all(6)
    print("Removing 6 and all duplicates:", sll.display())


if __name__ == "__main__":
    main()