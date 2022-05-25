# 내장 리스트로 구현한 Stack
# 내장 리스트의 단점인 공간 제약이 있다.

# 삽입, 삭제, 접근 모두 O(1)


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, x) -> None:
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.__stack)

    def print(self):
        print("Stack from top: ", end="")
        for i in range(len(self.__stack) - 1, -1, -1):
            print(self.__stack[i], end=" ")
        print()
