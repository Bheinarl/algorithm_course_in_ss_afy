def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_r = find(x)  # x root
    y_r = find(y)  # y root
    if x_r != y_r:
        parent[y_r] = x_r
        return True
    return False

n = int(input())
m = int(input())
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

parent = [i for i in range(n + 1)]

total_cost = 0
for cost, a, b in edges:
    if union(a, b):
        total_cost += cost

print(total_cost)