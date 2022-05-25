# 우선순위 큐
# 최소 힙

# 최소 힙의 조건
# 1. 완전 이진 트리
# 2. 모든 노드는 값을 갖고, 자식 노드(들) 값보다 작거나 같다.

# 삽입 연산
# 1. 리프(맨끝)에 원소 추가
# 2. 부모랑 비교해서 자식이 더 작으면 둘이 교체(재귀적으로 반복)(스며오르기)

# 삭제 연산
# 1. 루트(맨앞)를 맨끝의 원소로 교체
# 2. 자식이랑 비교해서 자식이 더 작으면 둘이 교체(재귀적으로 반복)(스며내리기)

# 힙 만들기 (buildHeap) - O(n)
# 삽입(insert) - O(log n)
# 삭제(deleteMin) - O(log n)
# 접근(min) - O(1)


class MinHeap:
    __A = None

    def __init__(self, lst):
        if lst == None:
            self.__A = []
        else:
            self.__A = lst
            self.buildHeap()

    # 삽입
    ## O(logn)
    def insert(self, x):
        self.__A.append(x)
        self.__percolate_up(len(self.__A) - 1)

    # 스며오르기
    def __percolate_up(self, i: int):
        parent = (i - 1) // 2  # 부모노드
        if i > 0 and self.__A[i] < self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolate_up(parent)

    # 힙에서 가장 작은(우선순위인) 원소 삭제
    ## O(logn)
    def deleteMin(self):
        if self.is_empty():
            raise IndexError("delete from empty heap")
        if self.size() == 1:
            return self.__A.pop()
        min = self.__A[0]  # 루트 노드
        self.__A[0] = self.__A.pop()  # 리스트의 끝 원소를 루트 노드로 옮긴 뒤 스며내리기 실행
        self.__percolate_down(0)
        return min

    # 스며내리기
    def __percolate_down(self, i: int):
        child = 2 * i + 1  # left child
        right_child = 2 * i + 2  # right child
        # 왼쪽 자식이 존재하면
        if child < len(self.__A):
            # 오른쪽 자식이 존재하고 왼쪽 자식보다 작으면 오른쪽 자식이랑 change
            if right_child < len(self.__A) and self.__A[child] > self.__A[right_child]:
                child = right_child

            if self.__A[i] > self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolate_down(child)

    # 최솟값 리턴 (루트 노드)
    def min(self):
        return self.__A[0]

    # 힙 만들기
    ## 마지막 층 노드 제외한 나머지에 스며내리기 적용
    ### O(n)
    def buildHeap(self):
        for i in range((len(self.__A) - 2) // 2, -1, -1):
            self.__percolate_down(i)

    def size(self) -> int:
        return len(self.__A)

    def is_empty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A = []
