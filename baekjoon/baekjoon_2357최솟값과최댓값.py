def find_max_value(start, end, node):
    if start == end:
        max_value_tree[node] = A[start]
        return max_value_tree[node]

    mid = (start + end) // 2
    max_value_tree[node] = max(find_max_value(start, mid, node * 2), find_max_value(mid+1, end, node * 2 + 1))
    return max_value_tree[node]

def find_min_value(start, end, node):
    if start == end:
        min_value_tree[node] = A[start]
        return min_value_tree[node]

    mid = (start + end) // 2
    min_value_tree[node] = min(find_min_value(start, mid, node * 2), find_min_value(mid+1, end, node * 2 + 1))
    return min_value_tree[node]

def interval_max_value(start, end, node, left, right):
    # 범위 밖
    if left > end or right < start:
        return -INF
    # 범위 안
    if left <= start and right >= end:
        return max_value_tree[node]
    mid = (start + end) // 2
    # start와 end가 바뀌면서 최댓값을 구해준다.
    return max(interval_max_value(start, mid, node*2, left, right), interval_max_value(mid+1, end, node*2+1, left, right))

def interval_min_value(start, end, node, left, right):
    # 범위 밖
    if left > end or right < start:
        return INF
    # 범위 안
    if left <= start and right >= end:
        return min_value_tree[node]
    mid = (start + end) // 2
    # start와 end가 바뀌면서 최댓값을 구해준다.
    return min(interval_min_value(start, mid, node*2, left, right), interval_min_value(mid+1, end, node*2+1, left, right))

A = [0]
INF = int(1e9)
N, M = map(int, input().split())
max_value_tree = [0] * (4 * N)
min_value_tree = [0] * (4 * N)
for _ in range(N):
    A.append(int(input()))
find_max_value(1, N, 1)
find_min_value(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(interval_min_value(1, N, 1, a, b), interval_max_value(1, N, 1, a, b))