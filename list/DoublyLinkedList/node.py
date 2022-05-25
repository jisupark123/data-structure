class Node:
    def __init__(self, new_item, prev: "Node", next: "Node"):
        self.item = new_item
        self.prev = prev
        self.next = next
