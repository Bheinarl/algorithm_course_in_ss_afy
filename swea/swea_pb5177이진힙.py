def enque(n):
    global last
    last += 1
    heap[last] = n  # 맨 마지막 노드에 넣고
    child_idx = last
    parent_idx = child_idx // 2
    while parent_idx >= 1 and heap[parent_idx] > heap[child_idx]:  # 부모 노드가 자식 노드보다 크면
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]  # 부모 노드와 자식 노드를 바꿔
        child_idx = parent_idx  # 자식 노드와 부모 노드 모두 한 단계 위로
        parent_idx = child_idx // 2


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    for num in ARR:
        enque(num)

    sum_ans = 0
    N //= 2  # 부모 노드의 인덱스는 //2 한 값
    while N >= 1:
        sum_ans += heap[N]
        N //= 2

    print(f'#{TEST_CASE} {sum_ans}')

"""
# 연결 리스트를 쓰는 메리트가 전혀 없다.
# 이진 트리를 뽑을 수는 있는데 이 값을 가지는 노드의 인덱스를 알려면 결국 또 리스트를 사용해야한다.

from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_lr(self.root, key)

    def insert_lr(self, node, key):

        queue = deque([node])

        while queue:

            node = queue.popleft()

            if key < node.key:
                node.key, key = key, node.key

            if node.left is None:
                node.left = Node(key)
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = Node(key)
                break
            else:
                queue.append(node.right)

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result

MH = MinHeap()
MH.insert(7)
print(MH.preorder_traversal())
MH.insert(2)
print(MH.preorder_traversal())
MH.insert(5)
print(MH.preorder_traversal())
MH.insert(3)
print(MH.preorder_traversal())
MH.insert(4)
print(MH.preorder_traversal())
MH.insert(6)
print(MH.preorder_traversal())
"""