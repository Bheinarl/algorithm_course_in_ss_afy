import sys
input = sys.stdin.readline

def make_tree(node, start, end):
    if start == end:  # leaf
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        make_tree(node * 2, start, mid)
        make_tree(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def change_num(node, start, end, idx, diff):
    if idx < start or idx > end:  # 범위 밖
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        change_num(node * 2, start, mid, idx, diff)
        change_num(node * 2 + 1, mid + 1, end, idx, diff)


def part_sum(node, start, end, left, right):
    if right < start or end < left:  # 겹치는 구간 없음
        return 0
    if left <= start and end <= right:  # 완전히 포함
        return tree[node]
    mid = (start + end) // 2
    return part_sum(node * 2, start, mid, left, right) + part_sum(node * 2 + 1, mid + 1, end, left, right)


n, m, k = map(int, input().split())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

tree = [0] * (4 * n)
make_tree(1, 1, n)

ans = []

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        change_num(1, 1, n, b, diff)
    else:  # a == 2
        ans.append(str(part_sum(1, 1, n, b, c)))

print("\n".join(ans))