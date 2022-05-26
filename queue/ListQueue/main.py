from Queue import Queue

a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a.front())
a.dequeue()
print(a)
