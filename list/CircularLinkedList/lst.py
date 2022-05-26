from node import Node

# 원형 연결 리스트
# 마지막 원소가 처음 원소를 가리킴
# 단순연결리스트와 다르게 head 대신 tail에 대한 정보를 가지고 있으므로 append() 연산에 강점을 보임
# 따라서 append() 연산이 필요한 extend(), copy(), reverse()가 훨씬 부담이 없어짐

# 접근(get) - O(n)
# 맨앞, 맨끝에 원소 추가(insert(0), append) - O(1)
# 그 밖의 원소 추가 - O(n)
# 삭제 (pop,remove) = O(n)


class List:
    def __init__(self):
        self.__tail = Node("dummy", None)  # tail에  가짜노드
        self.__tail.next = self.__tail  # 꼬리가 꼬리를 참조
        self.__cnt = 0  # 노드의 개수

    # i번째 인덱스에 원소 삽입
    def insert(self, i: int, new_item) -> None:
        if i >= 0 and i <= self.__cnt:  # Item이 3개 있으면 0,1,2,3 까지 허용
            prev = self.get_node(i - 1)
            new_node = Node(new_item, prev.next)
            prev.next = new_node
            if i == self.__cnt:  # 끝에 삽입하는 거라면 생성한 노드를 꼬리로 지정
                self.__tail = new_node
            self.__cnt += 1
        else:
            raise IndexError("list index out of range")

    # 리스트 끝에 원소 삽입
    def append(self, new_item):
        new_node = Node(new_item, self.__tail.next)
        self.__tail.next = new_node
        self.__tail = new_node
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
            prev = self.get_node(i - 1)
            deleted_item = prev.next.item
            prev.next = prev.next.next
            if i == self.__cnt - 1:  # 끝의 원소가 삭제되면 그 전의 원소가 tail로 바뀜
                self.__tail = prev
            self.__cnt -= 1
            return deleted_item
        else:
            raise IndexError("pop index out of range")

    # 가장 먼저 나오는 x 삭제 & 반환
    def remove(self, x):
        (prev, target) = self.__find_node(x)
        if target != None:
            prev.next = target.next
            if target == self.__tail:  # 끝의 원소가 삭제되면 그 전의 원소가 tail로 바뀜
                self.__tail = prev
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
        self.__tail == Node("dummy", None)
        self.__tail.next = self.__tail
        self.__cnt = 0

    def count(self, x) -> int:
        res = 0
        for element in self:
            if element == x:
                res += 1

        return res

    def extend(self, arr):  # arr은 순회 가능한 모든 객체
        for x in arr:
            self.append(x)

    def copy(self):
        res = List()
        for element in self:
            res.append(element)
        return res

    def reverse(self):
        __head = prev = self.__tail.next  # 맨 앞 노드
        curr = prev.next
        next = curr.next
        curr.next = __head
        __head.next = self.__tail
        self.__tail = curr
        for _ in range(self.__cnt - 1):
            prev = curr
            curr = next
            next = next.next
            curr.next = prev

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    def get_node(self, i: int) -> Node:
        node = self.__tail.next  # 맨 앞 노드
        for _ in range(i + 1):
            node = node.next
        return node

    def __find_node(self, x):
        __head = prev = self.__tail.next  # 맨 앞 노드
        target = prev.next  # 1번 노드
        while target != __head:
            if target.item == x:
                return (prev, target)
            else:
                prev, target = target, target.next
        return (None, None)

    def __str__(self):
        res = ""
        for element in self:
            res += f"{element}, "

        return "[" + res[:-2] + "]"

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
