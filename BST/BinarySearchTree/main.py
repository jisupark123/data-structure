from tree import Tree
from order import *

tree = Tree()
tree.insert(55)
tree.insert(15)
tree.insert(60)
tree.insert(8)
tree.insert(3)
tree.insert(28)
tree.insert(18)
tree.insert(45)
tree.insert(48)
tree.insert(50)
tree.insert(41)
tree.insert(30)
tree.insert(38)
tree.insert(33)
tree.insert(32)
tree.insert(36)
print(tree.count())
tree.insert(36)
print(tree.count())


# in_order(tree.get_root())

# tree.delete(28)
# print()
# in_order(tree.get_root())
