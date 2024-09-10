from collections import deque


def f(n, m):

    q = deque()
    q.append(n)
    visited = [-1]*1000001
    visited[n] = 0
    while q:
        now_n = q.popleft()
        lst = [now_n+1, now_n-1, now_n-10, now_n*2]
        if now_n == m:
            return visited[M]
        else:
            for j in range(4):
                new_n = lst[j]
                if new_n <= 1000000 and visited[new_n] == -1:
                    q.append(new_n)
                    visited[new_n] = visited[now_n] + 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    min_counts = abs(M-N)
    ans = f(N, M)

    print(f'#{TEST_CASE} {ans}')
