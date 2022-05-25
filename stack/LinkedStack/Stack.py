# 단순 연결리스트로 구현한 스택
# 스택 연산은 단순 연결리스트로 충분하다. (굳이 원형 리스트 사용할 필요 X)
# 단순 연결리스트는 맨 앞에 원소를 삽입할 때 O(1)의 효율을 보인다
# 따라서 push, pop, top 연산도 맨앞에서 진행한다.

# 삽입, 삭제, 접근 모두 O(1)


class Stack:
    def __init__(self):
        self.__list = List()

    def push(self, new_item):
        self.__list.insert(0, new_item)

    def pop(self):
        return self.__list.pop(0)

    def top(self):
        if self.is_empty():
            return None
        return self.__list.get(0)

    def pop_all(self):
        self.__list.clear()

    def is_empty(self):
        return self.__list.size() == 0

    def size(self) -> int:
        return self.__list.size()

    def print(self):
        print("Stack from top: ", end="")
        for i in range(self.__list.size()):
            print(self.__list.get(i), end=" ")
        print()


##############################################################
class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node


class List:
    def __init__(self):
        self.__head = Node("dummy", None)  # head에  가짜노드
        self.__cnt = 0  # 노드의 개수

    # i번째 인덱스에 원소 삽입
    def insert(self, i: int, new_item):
        if i >= 0 and i <= self.__cnt:  # Item이 3개 있으면 0,1,2,3 까지 허용
            prev = self.__get_node(i - 1)
            new_node = Node(new_item, prev.next)
            prev.next = new_node
            self.__cnt += 1
        else:
            raise IndexError("list index out of range")

    # 리스트 끝에 원소 삽입
    def append(self, new_item):
        prev = self.__get_node(self.__cnt - 1)
        new_node = Node(new_item, prev.next)
        prev.next = new_node
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
            prev = self.__get_node(i - 1)
            target = prev.next
            prev.next = target.next
            self.__cnt -= 1
            return target.item
        else:
            raise IndexError("list assignment index out of range")

    # 가장 먼저 나오는 x 삭제
    def remove(self, x):
        (prev, target) = self.__find_node(x)
        if target != None:
            prev.next = target.next
            self.__cnt -= 1
        else:
            raise ValueError(f"list.remove(x): {x} not in list")

    # i 번째 원소 알려주기
    def get(self, i: int):
        if self.is_empty():
            return None
        if i >= 0 and i < self.__cnt:
            return self.__get_node(i).item

    def index(self, x) -> int:
        node = self.__head.next  # 0번 노드
        for i in range(self.__cnt):
            if node.item == x:
                return i
            else:
                node = node.next

        return -1  # 없으면 -1 반환

    def is_empty(self) -> bool:
        return self.__cnt == 0

    def size(self) -> int:
        return self.__cnt

    def clear(self):
        self.__head == Node("dummy", None)
        self.__cnt = 0

    def count(self, x) -> int:
        res = 0
        node = self.__head.next
        for _ in range(self.__cnt):
            if node.item == x:
                res += 1
            node = node.next

        return res

    def extend(self, arr: "List"):
        for i in range(arr.size()):
            self.append(arr.get(i))

    def copy(self):
        res = List()
        for i in range(self.__cnt):
            res.append(self.get(i))
        return res

    def reverse(self):
        a = List()
        for i in range(self.__cnt):
            a.insert(0, self.get(i))
        self.clear()
        for i in range(a.size()):
            self.append(a.get(i))

    def sort(self) -> None:
        a = []
        for i in range(self.__cnt):
            a.append(self.get(i))
        a.sort()
        self.clear()
        for i in range(len(a)):
            self.append(a[i])

    def __get_node(self, i: int) -> Node:
        node = self.__head
        for _ in range(i + 1):
            node = node.next
        return node

    def __find_node(self, x):
        prev = self.__head  # 가짜 헤드
        target = prev.next  # 0번 노드
        while target != None:
            if target.item == x:
                return (prev, target)
            else:
                prev, target = target, target.next
        return (None, None)

    def print(self):
        res = ""
        node = self.__head.next
        for _ in range(self.__cnt - 1):
            res += f"{node.item}, "
            node = node.next

        print(f"[{res}{node.item}]")
