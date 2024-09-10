from collections import deque


def f(V):
    q = deque()
    visited = [0] * (V+1)
    lst = []
    for j in range(1, V+1):
        if ind[j] == 0:
            q.append(j)
            visited[j] += 1

    while q:
        k = q.popleft()
        lst.append(k)
        for p in adjL[k]:
            ind[p] -= 1
            if ind[p] == 0:
                q.append(p)
                visited[p] = visited[k] + 1

    return lst


T = 10
for TEST_CASE in range(1, T+1):
    V, E = map(int, input().split())
    ARR = list(map(int, input().split()))
    adjL = [[] for _ in range(V+1)]
    ind = [0] * (V+1)

    for i in range(E):
        n1, n2 = ARR[2*i], ARR[2*i+1]
        adjL[n1].append(n2)
        ind[n2] += 1

    ans_lst = f(V)

    print(f'#{TEST_CASE} ', end='')
    print(*ans_lst)
