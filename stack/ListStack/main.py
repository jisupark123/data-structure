from Stack import Stack

a = Stack()
for i in range(10):
    a.push(i + 1)
a.pop()
print(a.is_empty())
print(a)
