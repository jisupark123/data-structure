# 단순 연결리스트로 구현한 스택
# 스택 연산은 단순 연결리스트로 충분하다. (굳이 원형 리스트 사용할 필요 X)
# 단순 연결리스트는 맨 앞에 원소를 삽입할 때 O(1)의 효율을 보인다
# 따라서 push, pop, top 연산도 맨앞에서 진행한다.

# 삽입, 삭제, 접근 모두 O(1)


class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node


class Stack:
    def __init__(self):
        self.__head = Node("dummy", None)  # head에  가짜노드
        self.__cnt = 0  # 노드의 개수

    # 리스트 끝에 원소 삽입
    def push(self, new_item):
        prev = self.__head
        new_node = Node(new_item, prev.next)
        prev.next = new_node
        self.__cnt += 1

    def pop(self) -> Node:
        if self.is_empty():  # 리스트가 비었는지 확인
            raise IndexError("pop from empty list")
        prev = self.__head
        target = prev.next
        prev.next = target.next
        self.__cnt -= 1
        return target.item

    def top(self) -> Node:
        if self.is_empty():
            raise IndexError("stack index out of range")
        return self.__head.next.item

    def is_empty(self) -> bool:
        return self.__cnt == 0

    def size(self) -> int:
        return self.__cnt

    def clear(self):
        self.__head == Node("dummy", None)
        self.__cnt = 0

    def __str__(self):
        res = ""
        node = self.__head.next
        for _ in range(self.__cnt - 1):
            res += f"{node.item}, "
            node = node.next

        return f"stack([{res}{node.item}])"
