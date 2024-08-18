def f(s, g):
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        now_node = q.pop(0)

        for i in adjL[now_node]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[now_node] + 1

            if visited[i] > visited[now_node] + 1:  # 혹시 최솟값이 있으면 최솟값으로 변경
                visited[i] = visited[now_node] + 1

    if visited[g] == 0:  # 갈 수 없으면 0 반환
        return 0
    else:  # 갈 수 있으면 출발점 제외한 이동거리 visited[g] -1 반환
        return visited[g] - 1


T = int(input())
for TEST_CASE in range(1, T+1):
    V, E = map(int, input().split())

    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        V1, V2 = map(int, input().split())
        adjL[V1] += [V2]
        adjL[V2] += [V1]

    S, G = map(int, input().split())

    RESULT = f(S, G)

    print(f'#{TEST_CASE} {RESULT}')
