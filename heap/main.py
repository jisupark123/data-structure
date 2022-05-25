from maxHeap import MaxHeap
from minHeap import MinHeap


a = MaxHeap([1, 11, 9, 2, 5])
# for i in range(5):
#     print(a.deleteMax())
a = MinHeap([100, 1, 11, 9, 2, 5])
for i in range(7):
    print(a.deleteMin())
