from singly_linked_list import SinglyLinkedList, Node


class SplitEvensOdds(SinglyLinkedList):
    def split(self):
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        current = self.head

        evens_tail = None
        odds_tail = None

        while current:
            next_node = current.next
            current.next = None  

            if current.data % 2 == 0:
                if evens.head is None:
                    evens.head = current
                    evens_tail = current
                else:
                    evens_tail.next = current
                    evens_tail = current
            else:
                if odds.head is None:
                    odds.head = current
                    odds_tail = current
                else:
                    odds_tail.next = current
                    odds_tail = current

            current = next_node

        self.head = None

        return evens, odds