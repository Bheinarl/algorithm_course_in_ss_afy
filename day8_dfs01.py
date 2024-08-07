"""
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
"""
adjl[0] X
adjl[1] -> 1에 인접인 정점

...

adjl = [ [], [2, 3] ... ]
"""


def dfs(s, v):                   # s는 시작정점, V는 정점개수(마지막정점)
    visited = [0] * (v + 1)      # 방문한 정점을 표시
    stack = []                   # 스택 생성
    visited[s] = 1               # 시작정점 방문표시
    v = s
    while True:
        for w in adjL[v]:        # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push 하고
                v = w            # w에 방문
                visited[w] = 1   # w에 방문 표시
                break            # for w 에 대한 break
        else:                    # 남은 인접 정점이 없어서 break 가 걸리지 않은 경우
            if stack:            # stack 에 원소가 남아있으면 True
                                 # 이전 갈림길을 스택에서 꺼내서(append, pop을 쓰는 경우) if TOP > -1 (TOP 을 쓰는 경우)
                v = stack.pop()
            else:                # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
                break            # while 문에 대한 break


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    dfs(1, V)