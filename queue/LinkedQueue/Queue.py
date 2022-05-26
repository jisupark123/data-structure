# 원형 연결 리스트를 이용한 큐
# 원형 연결리스트는 맨 앞과 맨 끝에 원소를 삽입할 때 O(1)의 효율을 보인다. -> 큐에 적합한 자료구조

# 삽입, 삭제, 접근 모두 O(1)


class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node


class Queue:
    def __init__(self):
        self.__tail = Node("dummy", None)  # tail에  가짜노드
        self.__tail.next = self.__tail  # 꼬리가 꼬리를 참조
        self.__cnt = 0  # 노드의 개수

    # 큐 끝에 원소 삽입
    def enqueue(self, new_item):
        new_node = Node(new_item, self.__tail.next)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__cnt += 1

    # 맨 앞의 원소 삭제 && 리턴
    def dequeue(self) -> "Node":
        if self.__cnt == 0:
            raise IndexError("dequeue from empty list")
        prev = self.__tail.next
        deleted_item = prev.next.item
        prev.next = prev.next.next
        self.__cnt -= 1
        return deleted_item

    def front(self) -> "Node":
        if self.__cnt == 0:
            raise IndexError("queue index out of range")
        return self.__tail.next.next.item

    def is_empty(self) -> bool:
        return self.__cnt == 0

    def size(self) -> int:
        return self.__cnt

    def clear(self):
        self.__tail == Node("dummy", None)
        self.__tail.next = self.__tail
        self.__cnt = 0

    def get_node(self, i: int) -> "Node":
        node = self.__tail.next  # 맨 앞 노드
        for _ in range(i + 1):
            node = node.next
        return node

    def __str__(self):
        res = ""
        for element in self:
            res += f"{element}, "

        return f"queue([{res[:-2]}])"

    def __iter__(self):
        return ListIterator(self)


class ListIterator:
    def __init__(self, queue: Queue):
        self.__head = queue.get_node(-1)  # 가짜 헤드
        self.iterPosition = self.__head.next  # 0번 노드

    def __next__(self):
        if self.iterPosition == self.__head:  # 순환 끝
            raise StopIteration
        else:  # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
