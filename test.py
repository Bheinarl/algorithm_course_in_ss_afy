from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            now_node = queue.popleft()

            if now_node.left is None:
                now_node.left = new_node
                break
            else:
                queue.append(now_node.left)

            if now_node.right is None:
                now_node.right = new_node
                break
            else:
                queue.append(now_node.right)

    def inorder_traversal(self):
        return self.result_inorder_traversal(self.root, [])

    def result_inorder_traversal(self, now_node, result):
        if now_node:
            self.result_inorder_traversal(now_node.left, result)
            result.append(now_node.key)
            self.result_inorder_traversal(now_node.right, result)
        return result


for TEST_CASE in range(1, 11):
    N = int(input())

    txt = []
    ARR = []

    child_L = [0] * (N+1)
    child_R = [0] * (N+1)

    for i in range(N):
        lst = list(input().split())
        txt += [lst[1]]  # 입력 순서대로 글자 저장
        lst[0] = int(lst[0])

    tree = BinaryTree()

    for j in range(N):
        tree.insert(txt[j])

    text_arr = tree.inorder_traversal()

    print(f'#{TEST_CASE} ', end='')
    for m in range(N):
        print(text_arr[m], end='')
    print()
