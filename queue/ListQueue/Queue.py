# 내장 리스트로 구현한 큐
# 내장 리스트의 단점인 공간 제약이 있다.

# 삽입, 삭제, 접근 모두 O(1)


class Queue:
    def __init__(self):
        self.__queue = []

    # 큐의 끝에 원소 추가
    def enqueue(self, x):
        self.__queue.append(x)

    # 큐의 첫 원소를 삭제한 후 원소 리턴
    def dequeue(self):
        return self.__queue.pop(0)

    ## 큐 초기화
    def dequeueAll(self):
        self.__queue.clear()

    # 큐의 첫 원소를 알려줌
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]

    def isEmpty(self) -> bool:
        return not bool(self.__queue)

    def print(self):
        print("Queue from front: ", end="")
        for i in range(len(self.__queue)):
            print(self.__queue[i], end=" ")
        print()
