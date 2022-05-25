# 전위순회, 중위순회, 후위순회

from node import Node

# class Order:

# 전위순회
def pre_order(node: Node):
    if node != None:
        print(node.item)
        pre_order(node.left)
        pre_order(node.right)


# 중위순회
def in_order(node: Node):
    if node != None:
        in_order(node.left)
        print(node.item)
        in_order(node.right)


# 후위순회
def post_order(node: Node):
    if node != None:
        post_order(node.left)
        post_order(node.right)
        print(node.item)
