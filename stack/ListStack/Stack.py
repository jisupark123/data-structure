# 내장 리스트로 구현한 Stack
# 내장 리스트의 단점인 공간 제약이 있다.

# 삽입, 삭제, 접근 모두 O(1)


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, x) -> None:
        self.__stack.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty list")
        return self.__stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("stack index out of range")
        else:
            return self.__stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.__stack)

    def __str__(self):
        res = ""
        for element in self.__stack:
            res += f"{element}, "
        return f"stack([{res[:-2]}])"
