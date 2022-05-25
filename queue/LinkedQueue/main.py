from Queue import Queue

a = Queue()
for i in range(5):
    a.enqueue(i + 1)

a.dequeue()
a.print()
