# 양방향에서 요소를 추가하고 제거할 수 있는 양방향 큐
# 이중 연결리스트로 구현한다.
# 일반적인 큐보다 다양한 곳에서 사용할 수 있다.
# 이중 연결 리스트를 사용했기 때문에 메모리 공간을 더 차지한다.
# 삽입, 삭제, 접근 모두 O(1)


class Node:
    def __init__(self, new_item, prev: "Node", next: "Node"):
        self.item = new_item
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self):
        self.__head = Node("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__cnt = 0  # 노드의 개수

    # 리스트 끝에 원소 삽입
    def append(self, new_item) -> None:
        prev = self.__head.prev
        new_node = Node(new_item, prev, self.__head)
        prev.next = new_node
        self.__head.prev = new_node
        self.__cnt += 1

    # 리스트 앞에 원소 삽입
    def appendleft(self, new_item) -> None:
        next = self.__head.next
        new_node = Node(new_item, self.__head, next)
        self.__head.next = new_node
        next.prev = new_node
        self.__cnt += 1

    # 맨 끝 원소 삭제 & 반환
    def pop(self) -> Node:
        if self.is_empty():  # 리스트가 비었는지 확인
            raise IndexError("pop from empty deque")

        target = self.__head.prev
        target.prev.next = target.next
        target.next.prev = target.prev
        self.__cnt -= 1
        return target.item

    # 맨 앞의 원소 삭제 & 반환
    def popleft(self) -> Node:
        target = self.__head.next  # 0번째 원소
        target.prev.next = target.next
        target.next.prev = target.prev
        return target.item

    # 가장 먼저 나오는 x 삭제 & 반환
    def remove(self, x):
        target = self.__find_node(x)
        if target != None:
            target.prev.next = target.next
            target.next.prev = target.prev
            self.__cnt -= 1
            return x
        else:
            raise ValueError(f"deque.remove(x): {x} not in deque")

    def front(self):
        if self.__cnt == 0:
            raise IndexError("deque index out of range")
        return self.__head.next.item

    def end(self):
        if self.__cnt == 0:
            raise IndexError("deque index out of range")
        return self.__head.prev.item

    def index(self, x) -> int:
        res = 0
        for element in self:
            if element == x:
                return res
            res += 1

        return -1  # 없으면 -1 반환

    def is_empty(self) -> bool:
        return self.__cnt == 0

    def size(self) -> int:
        return self.__cnt

    def clear(self):
        self.__head = Node("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__cnt = 0  # 노드의 개수

    def count(self, x) -> int:
        res = 0
        for element in self:
            if element == x:
                res += 1

        return res

    def extend(self, arr):  # arr은 순회 가능한 모든 객체
        for element in arr:
            self.append(element)

    # 왼쪽에서 확장
    def extendleft(self, arr):  # arr은 순회 가능한 모든 객체
        for i in range(len(arr) - 1, -1, -1):
            self.appendleft(arr[i])

    def copy(self) -> Node:
        res = Deque()
        for element in self:
            res.append(element)
        return res

    def reverse(self) -> None:
        prev = self.__head
        curr = prev.next
        next = curr.next
        self.__head.next = prev.prev
        self.__head.prev = curr
        for _ in range(self.__cnt):
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
            next = next.next

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    # 인덱스가 오른쪽에 가까우면 오른쪽부터 순회
    # 왼쪽에 가까우면 왼쪽부터 순회
    def get_node(self, i: int) -> Node:
        node = self.__head
        if i <= self.__cnt // 2:
            for _ in range(i + 1):
                node = node.next
            return node
        else:
            for _ in range(self.__cnt - i):
                node = node.prev
            return node

    def __find_node(self, x):
        target = self.__head.next  # 0번 노드
        while target != self.__head:
            if target.item == x:
                return target
            else:
                target = target.next
        return None

    def __str__(self) -> None:
        res = ""
        for element in self:
            res += f"{element}, "

        return f"deque([{res[:-2]}])"

    def __iter__(self):
        return ListIterator(self)


class ListIterator:
    def __init__(self, lst: Deque):
        self.__head = lst.get_node(-1)  # 가짜 헤드
        self.iterPosition = self.__head.next  # 0번 노드

    def __next__(self):
        if self.iterPosition == self.__head:  # 순환 끝
            raise StopIteration
        else:  # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
