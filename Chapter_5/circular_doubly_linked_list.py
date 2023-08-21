#
# 4. an example of a circular doubly linked list in Python:
#

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node

    def print_list(self):
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node is self.head:
                break
        print()

    def print_reverse_list(self):
        current_node = self.head.prev
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.prev
            if current_node is self.head.prev:
                break
        print()

#
# Create a new circular doubly linked list
cdllist = CircularDoublyLinkedList()

# Add nodes to the circular doubly linked list
cdllist.add_node(1)
cdllist.add_node(2)
cdllist.add_node(3)

# Print the circular doubly linked list
cdllist.print_list() # Output: 1 2 3 (circles back to 1)

# Print the circular doubly linked list in reverse order
cdllist.print_reverse_list() # Output: 3 2 1 (circles back to 3)

"""
참고: https://couplewith.tistory.com/390
"""