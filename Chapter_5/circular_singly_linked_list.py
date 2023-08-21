#
# 3. an example of a circular singly linked list in Python:
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head

    def print_list(self):
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node is self.head:
                break
        print()



# Create a new circular singly linked list
clist = CircularLinkedList()

# Add nodes to the circular singly linked list
clist.add_node(1)
clist.add_node(2)
clist.add_node(3)

# Print the circular singly linked list
clist.print_list() # Output: 1 2 3  (circles back to 1)

"""
참고: https://couplewith.tistory.com/390
"""