from node import Node

# AVL 검색 트리

# 이진 검색 트리의 특성
# 1. 각 노드는 킷값을 하나씩 갖는다. 각 노드의 킷값은 모두 다르다.
# 2. 최상위 레벨에 루트 노드가 있고, 각 노드는 최대 2개의 자식 노드를 갖는다.
# 3. 임의 노드의 킷값은 자신의 왼쪽 아래에 있는 모든 노드의 킷값보다 크고, 오른쪽 아래에 있는 모든 노드의 킷값보다 작다.

# AVL 검색 트리는 Basic 이진 검색 트리의 단점을 보완한 자료구조다.
# 삽입, 삭제 연산 시 트리의 균형을 체크, 만약 이상이 있으면 잡아주는 연산을 추가로 수행한다.
# AVL 검색 트리 역시 삽입, 검색, 삭제 모두 O(log n)의 시간복잡도를 가진다.

# 균형이 깨지는 조건 - 임의의 노드의 왼쪽 자식의 개수가 오른쪽 자식과 2이상 차이날 때
# 트리 수선 방법 -
# 왼쪽 자식과 오른쪽 자식의 균형이 깨진 임의의 노드를 t라고 가정한다.
# t를 기준으로 하는 트리 수선 작업은 t의 네 손자 서브 트리 중 가장 깊은 것에 따라 다음 네 가지 유형으로 나뉜다.

# LL타입 - t.left.left가 가장 깊음 - 해결방법: node를 기준으로 우회전 한번
# LR타입 - t.left.right가 가장 깊음 - 해결방법: node.left를 기준으로 좌회전 한번, node를 기준으로 우회전 한번
# RR타입 - t.right.right가 가장 깊음 - 해결방법: node를 기준으로 좌회전 한번
# RL타입 - t.right.left가 가장 깊음 - 해결방법: node.right를 기준으로 우회전 한번, node를 기준으로 좌회전 한번


class Tree:
    def __init__(self):
        self.__NIL = Node(None, None, None, 0)  # left = None, right = None 대신 참조할 노드
        self.__root = self.__NIL
        self.__count = 0  # 노드의 개수

        # 식별용 변수
        self.LL = 1
        self.LR = 2
        self.RR = 3
        self.RL = 4
        self.NO_NEED = 0
        self.ILLEGAL = -1

    # 검색
    def search(self, x):
        res = self.__search_item(self.__root, x)
        if res != self.__NIL:
            return res
        else:
            print(f"{x}은(는) 존재하지 않는 키입니다!")
            return None

    def __search_item(self, node: Node, x) -> Node:
        if node == self.__NIL:  # 없는 노드면
            return self.__NIL
        elif x == node.item:
            return node
        elif x < node.item:
            return self.__search_item(node.left, x)
        else:
            return self.__search_item(node.right, x)

    def insert(self, x):
        self.__root = self.__insert_item(self.__root, x)

    def __insert_item(self, node: Node, x) -> Node:
        if node == self.__NIL:
            node = Node(x, self.__NIL, self.__NIL, 1)
            self.__count += 1
        elif x < node.item:  # 왼쪽 가지로
            node.left = self.__insert_item(node.left, x)
            node.height = 1 + max(node.right.height, node.left.height)
            type = self.__check_balance(node)  # 수선할 AVL 타입 체크 (LL,LR,RR,RL)
            if type != self.NO_NEED:
                node = self.__balance_avl(node, type)
        elif x > node.item:  # 오른쪽 가지로
            node.right = self.__insert_item(node.right, x)
            node.height = 1 + max(node.right.height, node.left.height)
            type = self.__check_balance(node)  # 수선할 AVL 타입 체크 (LL,LR,RR,RL)
            if type != self.NO_NEED:
                node = self.__balance_avl(node, type)
        else:  # 중복되는 값 (x == node.item)
            print(f"{node.item}은(는) 중복되는 키이므로 insert 연산을 수행할 수 없습니다")
        return node

    def delete(self, x):
        pre_cnt = self.__count
        self.__root = self.__delete_item(self.__root, x)
        if pre_cnt == self.__count:  # 이전 노드 개수랑 연산 후 노드 개수가 같으면
            print(f"{x}은(는) 존재하지 않는 키입니다!")

    def __delete_item(self, node: Node, x) -> Node:
        if node == self.__NIL:
            return self.__NIL  # Item not found!
        if x == node.item:
            node = self.__delete_node(node)
            self.__count -= 1
        elif x < node.item:  # 왼쪽 가지로
            node.left = self.__delete_item(node.left, x)
            node.height = 1 + max(node.right.height, node.left.height)
            type = self.__check_balance(node)  # 수선할 AVL 타입 체크 (LL,LR,RR,RL)
            if type != self.NO_NEED:
                node = self.__balance_avl(node, type)
        else:  # 오른쪽 가지로
            node.right = self.__delete_item(node.right, x)
            node.height = 1 + max(node.right.height, node.left.height)
            type = self.__check_balance(node)  # 수선할 AVL 타입 체크 (LL,LR,RR,RL)
            if type != self.NO_NEED:
                node = self.__balance_avl(node, type)
        return node

    def __delete_node(self, node: Node) -> Node:
        if node.left == self.__NIL and node.right == self.__NIL:  # case 1(자식이 없음)
            return self.__NIL
        elif node.left == self.__NIL:  # case 2(오른자식뿐)
            return node.right
        elif node.right == self.__NIL:  # case 2(왼자식뿐)
            return node.left
        else:  # case 3(두 자식이 다 있음)
            (item, R_node) = self.__delete_min_item(node.right)
            node.item = item
            node.right = R_node
            node.height = self.__height(node)
            type = self.__check_balance(node)
            if type != self.NO_NEED:
                node = self.__balance_avl(node, type)
            return node

    def __delete_min_item(self, node: Node) -> tuple:
        if node.left == self.__NIL:  # 찾음
            return (node.item, node.right)

        (item, L_node) = self.__delete_min_item(node.left)
        node.left = L_node
        node.height = self.__height(node)
        type = self.__check_balance(node)
        if type != self.NO_NEED:
            node = self.__balance_avl(node, type)
        return (node, item)

    # 균형 잡기
    def __balance_avl(self, node: Node, type: int) -> Node:
        return_node = self.__NIL
        if type == self.LL:  ## LL이면 node를 기준으로 우회전 한번
            return_node = self.__right_rotate(node)
        elif type == self.LR:  ## LR이면 node.left를 기준으로 좌회전 한번, node를 기준으로 우회전 한번
            node.left = self.__left_rotate(node.left)
            return_node = self.__right_rotate(node)
        elif type == self.RR:  ## RR이면 node를 기준으로 좌회전 한번
            return_node = self.__left_rotate(node)
        elif type == self.RL:  ## RL이면 node.right를 기준으로 우회전 한번, node를 기준으로 좌회전 한번
            node.right = self.__right_rotate(node.right)
            return_node = self.__left_rotate(node)
        else:
            print("Imposible type! Should be one of LL,LR,RR,RL")

        return return_node

    # 좌회전
    def __left_rotate(self, node: Node) -> Node:
        R_child: Node = node.right
        if R_child == self.__NIL:
            raise Exception(node.item + "'s RChild shouldn't be NIL!")  # 논리 오류
        RL_child = R_child.left
        R_child.left = node
        node.right = RL_child
        node.height = 1 + max(node.left.height, node.right.height)
        R_child.height = 1 + max(R_child.left.height, R_child.right.height)
        return R_child

    # 우회전
    def __right_rotate(self, node: Node) -> Node:
        L_child: Node = node.left
        if L_child == self.__NIL:
            raise Exception(node.item + "'s RChild shouldn't be NIL!")  # 논리 오류
        LR_child = L_child.right
        L_child.right = node
        node.left = LR_child
        node.height = 1 + max(node.left.height, node.right.height)
        L_child.height = 1 + max(L_child.left.height, L_child.right.height)
        return L_child

    # 필요한 수선을 체크 후 반환 (LL,LR,RR,RL)
    def __check_balance(self, node: Node) -> int:
        type = self.ILLEGAL

        if node.left.height >= node.right.height + 2:  # L 유형
            if node.left.left.height >= node.left.right.height:
                type = self.LL
            else:
                type = self.LR
        elif node.right.height >= node.left.height + 2:  # R 유형
            if node.right.right.height >= node.right.left.height:
                type = self.RR
            else:
                type = self.RL
        else:
            type = self.NO_NEED
        return type

    # 노드의 높이
    def __height(self, node: Node) -> int:
        return 1 + max(node.left.height, node.right.height)

    def is_empty(self) -> bool:
        return self.__root == self.__NIL

    def clear(self):
        self.__root = self.__NIL

    def get_root(self):
        return self.__root

    # 전위순회
    def pre_order(self, node: Node):
        if node != self.__NIL:
            print(node.item)
            self.pre_order(node.left)
            self.pre_order(node.right)

    # 중위순회
    def in_order(self, node: Node):
        if node != self.__NIL:
            self.in_order(node.left)
            print(node.item)
            self.in_order(node.right)

    # 후위순회
    def post_order(self, node: Node):
        if node != self.__NIL:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.item)

    def count(self) -> int:
        return self.__count
