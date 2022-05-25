from node import Node

# 이중 && 원형 연결 리스트
# 노드를 찾을 때 앞으로 찾거나 뒤로 찾을 수도 있어서 최대 반만큼 빠르다.
# 하지만 이외의 연산은 원형 연결 리스트랑 똑같고 괜히 공간만 더 차지해서 별로 좋아보이진 않는다.


class List:
    def __init__(self):
        self.__head = Node("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__cnt = 0  # 노드의 개수

    # i번째 인덱스에 원소 삽입
    def insert(self, i: int, new_item) -> None:
        if i >= 0 and i <= self.__cnt:  # Item이 3개 있으면 0,1,2,3 까지 허용
            prev = self.get_node(i - 1)
            new_node = Node(new_item, prev, prev.next)
            new_node.next.prev = new_node
            prev.next = new_node
            self.__cnt += 1
        else:
            raise IndexError("list index out of range")

    # 리스트 끝에 원소 삽입
    def append(self, new_item) -> None:
        prev = self.__head.prev
        new_node = Node(new_item, prev, self.__head)
        prev.next = new_node
        self.__head.prev = new_node
        self.__cnt += 1

    # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
    # 매개변수가 주어지면 해당 인덱스 원소 삭제 & 반환
    def pop(self, *args) -> Node:
        if self.is_empty():  # 리스트가 비었는지 확인
            raise IndexError("pop from empty list")
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:  # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
            i = self.__cnt - 1
        if i >= 0 and i < self.__cnt:
            target = self.get_node(i)
            target.prev.next = target.next
            target.next.prev = target.prev
            self.__cnt -= 1
            return target.item
        else:
            raise IndexError("pop index out of range")

    # 가장 먼저 나오는 x 삭제 & 반환
    def remove(self, x):
        target = self.__find_node(x)
        if target != None:
            target.prev.next = target.next
            target.next.prev = target.prev
            self.__cnt -= 1
            return x
        else:
            raise ValueError(f"list.remove(x): {x} not in list")

    # 매개변수가 없거나 -1이면 마지막 원소를 반환
    # 매개변수가 주어지면 해당 인덱스의 원소를 반환
    def get(self, *args):
        if self.is_empty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__cnt - 1
        if i >= 0 and i < self.__cnt:
            return self.get_node(i).item
        else:
            raise IndexError("list index out of range")

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

    def copy(self) -> Node:
        res = List()
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

    def get_node(self, i: int) -> Node:
        node = self.__head
        for _ in range(i + 1):
            node = node.next
        return node

    def __find_node(self, x):
        target = self.__head.next  # 0번 노드
        while target != self.__head:
            if target.item == x:
                return target
            else:
                target = target.next
        return None

    def print(self) -> None:
        res = ""
        for element in self:
            res += f"{element}, "

        print("[" + res[:-2] + "]")

    def __iter__(self):
        return ListIterator(self)


class ListIterator:
    def __init__(self, lst: List):
        self.__head = lst.get_node(-1)  # 가짜 헤드
        self.iterPosition = self.__head.next  # 0번 노드

    def __next__(self):
        if self.iterPosition == self.__head:  # 순환 끝
            raise StopIteration
        else:  # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
