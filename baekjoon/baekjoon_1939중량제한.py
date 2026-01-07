import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

start, end = map(int, input().split())

edges.sort(reverse=True)

parent = list(range(N + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

for w, a, b in edges:
    union(a, b)
    if find(start) == find(end):
        print(w)
        break