from Stack import Stack

a = Stack()
for i in range(10):
    a.push(i + 1)
print(a.is_empty())
a.print()
