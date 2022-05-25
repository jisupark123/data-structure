# 개방 주소 해시 테이블
# 따로 원형리스트를 만들지 않으므로 공간 낭비 X
# 빈자리가 나올 때까지 hash를 반복한다.
# 저장, 검색, 삭제 모두 O(1)의 시간복잡도를 가진다.

# 체이닝 방법과 달리 적재율이 절대 1을 넘을 수 없다.
# 적재율이 높아질수록 해싱의 효율이 떨어진다.
# 개방 주소 방법에서는 보통 적재율의 상한을 정해놓고
# 이를 넘으면 해시 테이블 크기를 2배 가까이 키우고 다시 해싱하여 저장하는데 흔히 a = 1/2을 경계치로 설정한다.
# 해시테이블은 저장과 검색 시 궁극적으로 O(1)의 시간을 지향하므로 적재율이 너무 높아지지 않게 통제하는 것이 좋다.


class HashTable:
    def __init__(self, n: int):
        self.__table = [None for _ in range(n)]
        self.__cnt = 0
        self.__DELETED = -54321
        self.__NOT_FOUND = -12345

    def __hash(self, i: int, x):
        return (x + i) % len(self.__table)

    def insert(self, x):
        if self.__cnt == len(self.__table):
            raise MemoryError("해시 테이블 용량 초과")

        else:
            for i in range(len(self.__table)):
                slot = self.__hash(i, x)

                # 빈자리면
                if self.__table[slot] == None or self.__table[slot] == self.__DELETED:
                    self.__table[slot] = x
                    self.__cnt += 1
                    break

    def search(self, x) -> int:
        for i in range(len(self.__table)):
            slot = self.__hash(i, x)
            if self.__table[slot] == None:
                raise ValueError(f"{x} is not in table")
            if self.__table[slot] == x:
                return slot
        raise ValueError(f"{x} is not in table")

    def delete(self, x):
        for i in range(len(self.__table)):
            slot = self.__hash(i, x)
            if self.__table[slot] == None:
                raise ValueError("table.remove(x): x not in table")
            if self.__table[slot] == x:  # 찾으면 원래 값을 없애고 Deleted 표시
                self.__table[slot] = self.__DELETED
                self.__cnt -= 1
                break
