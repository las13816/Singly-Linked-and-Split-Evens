class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

  
    def build_list_forward(self, values):
        for value in values:
            self.insert_end(value)

    
    def build_list_backward(self, values):
        for value in values:
            self.insert_front(value)

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def remove_all(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        current = self.head
        output = "Head -> "
        while current:
            output += f"{current.data} -> "
            current = current.next
        output += "None"
        return output

    
    def display_reverse_nr(self):
        stack = []
        current = self.head

        while current:
            stack.append(current.data)
            current = current.next

        output = "None <- "
        while stack:
            output += f"{stack.pop()} -> "
        output = output.rstrip(" -> ")
        output += " <- Head"
        return output