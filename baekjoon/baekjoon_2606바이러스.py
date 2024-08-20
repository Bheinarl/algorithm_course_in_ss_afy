def dfs(v):
    stack = []
    visited = [0] * (v+1)
    now_v = 1
    visited[now_v] = 1

    while True:
        for w in adjL[now_v]:
            if visited[w] == 0:
                stack.append(now_v)
                now_v = w
                visited[now_v] = 1
                break
        else:
            if stack:
                now_v = stack.pop()
            else:
                break

    result = sum(visited) - 1
    return result


V = int(input())
e = int(input())

adjL = [[] for _ in range(V+1)]

for i in range(e):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

RESULT = dfs(V)
print(RESULT)
