import sys

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

N, M = map(int, sys.stdin.readline().split())
LST = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    LST.append((C, A, B))

LST.sort()
cost = 0  # 비용

parent = [i for i in range(N+1)]

for C, A, B in LST:
    if not same_parent(A, B):
        union_parent(A, B)
        cost += C
        max_cost = C  # 마지막 간선을 기록

print(cost - max_cost)  # 마을을 2개로 분리해야하므로 가장 비용이 큰 도로를 없애면 된다.