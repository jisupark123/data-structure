from Queue import Queue

a = Queue()
for i in range(10):
    a.enqueue(i + 1)

a.dequeue()
print(a.front())
print(a)
