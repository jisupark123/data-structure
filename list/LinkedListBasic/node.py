class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node
