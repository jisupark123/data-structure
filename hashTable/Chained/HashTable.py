# 체이닝 해시 테이블
# 주소마다 하나의 원형 리스트가 있다
# 같은 주소를 가진 원소가 하나의 원형 리스트에 모두 저장된다.
# 저장, 검색, 삭제 모두 O(1)의 시간복잡도를 가진다.

# 체이닝 방법을 이용하는 해싱에서 적재율이 a일 때, 탐색 횟수의 기대치는 a에 비례한다.
# 개방 주소 방법과 달리 적재율에 제한이 없지만 그래도 적재율이 높아질수록 해싱의 효율이 떨어진다.
# 해시테이블은 저장과 검색 시 궁극적으로 O(1)의 시간을 지향하므로 적재율이 너무 높아지지 않게 통제하는 것이 좋다.


class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node


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
    def pop(self, *args) -> "Node":
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

    def get_node(self, i: int) -> "Node":
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

    def print(self):
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

    def __init__(self):
        self.__head = Node("dummy", None)  # head에  가짜노드
        self.__cnt = 0  # 노드의 개수

    # i번째 인덱스에 원소 삽입
    def insert(self, i: int, new_item):
        if i >= 0 and i <= self.__cnt:  # Item이 3개 있으면 0,1,2,3 까지 허용
            prev = self.get_node(i - 1)
            new_node = Node(new_item, prev.next)
            prev.next = new_node
            self.__cnt += 1
        else:
            raise IndexError("list index out of range")

    # 리스트 끝에 원소 삽입
    def append(self, new_item):
        prev = self.get_node(self.__cnt - 1)
        new_node = Node(new_item, prev.next)
        prev.next = new_node
        self.__cnt += 1

    # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
    # 매개변수가 주어지면 해당 인덱스 원소 삭제 & 반환
    def pop(self, *args) -> "Node":
        if self.is_empty():  # 리스트가 비었는지 확인
            raise IndexError("pop from empty list")
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:  # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
            i = self.__cnt - 1
        if i >= 0 and i < self.__cnt:
            prev = self.get_node(i - 1)
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
            return self.get_node(i).item

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

    def get_node(self, i: int) -> Node:
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


class HashTable:
    def __init__(self, n):
        self.__table = [List() for _ in range(n)]
        self.__cnt = 0

    def __hash(self, x: int):  # 편의상 int 타입으로 제한
        return x % len(self.__table)

    def insert(self, x: int):
        slot = self.__hash(x)
        self.__table[slot].insert(0, x)
        self.__cnt += 1

    def search(self, x: int) -> "Node":
        slot = self.__hash(x)
        if self.__table[slot].is_empty():
            return None
        else:
            head = prev = self.__table[slot].get_node(-1)  # 더미 헤드
            curr = prev.next
            while curr != head:
                if curr.item == x:
                    return curr
                else:
                    prev, curr = curr, curr.next

            return None

    def delete(self, x: int):
        slot = self.__hash(x)
        try:
            self.__table[slot].remove(x)
            self.__cnt -= 1
        except:
            raise ValueError("list.remove(x): x not in list")

    def isEmpty(self):
        return self.__cnt == 0

    def clear(self):
        for i in range(len(self.__table)):
            self.__table[i] = List()
        self.___cnt = 0

    def size(self):
        return self.__cnt
