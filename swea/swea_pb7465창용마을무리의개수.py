def dfs(n):
    visited[n] = 1

    for i in adjL[n]:
        if visited[i] == 0:
            dfs(i)


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N+1)

    adjL = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjL[a].append(b)
        adjL[b].append(a)

    counts = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            counts += 1

    print(f'#{TEST_CASE} {counts}')
