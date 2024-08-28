def f(i, j, s, dig):  # i, j는 지금 내 좌표 / s는 지금까지 이동한 거리 / dig는 땅 파낸 횟수

    global max_dist

    visited[i][j] = 1

    if max_dist < s+1:
        max_dist = s+1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if ARR[i][j] > ARR[ni][nj]:
                f(ni, nj, s+1, dig)
            # 어떻게어떻게 dig = 1일 때랑 구분지어서 하려고 했는데
            # dig한 직후랑 dig한 다음이랑 처리하는 방법이 없어서 dig했다가 다시 복구하는 방법이 맞는듯
            elif dig == 0 and ARR[i][j] > ARR[ni][nj] - K:
                temp_height = ARR[ni][nj]
                ARR[ni][nj] = ARR[i][j] - 1  # 필요한만큼만
                f(ni, nj, s+1, 1)
                ARR[ni][nj] = temp_height

    visited[i][j] = 0


T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    sp = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if ARR[i][j] == max_height:
                sp += [[i, j]]
            elif ARR[i][j] > max_height:
                max_height = ARR[i][j]
                sp = [[i, j]]

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    visited = [[0]*N for _ in range(N)]
    max_dist = 0

    for arr in sp:
        [i, j] = arr
        f(i, j, 0, 0)

    print(f'#{TEST_CASE} {max_dist}')

"""
def dfs(s, v):  # s는 시작정점, V는 정점개수(마지막정점)
    visited = [0] * (v + 1)  # 방문한 정점을 표시
    stack = []  # 스택 생성
    visited[s] = 1  # 시작정점 방문표시
    v = s
    while True:
        for w in adjL[v]:  # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push 하고
                v = w  # w에 방문
                visited[w] = 1  # w에 방문 표시
                break  # for w 에 대한 break
        else:  # 남은 인접 정점이 없어서 break 가 걸리지 않은 경우
            if stack:  # stack 에 원소가 남아있으면 True
                # 이전 갈림길을 스택에서 꺼내서(append, pop을 쓰는 경우) if TOP > -1 (TOP 을 쓰는 경우)
                v = stack.pop()
            else:  # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
                break
"""
"""
k만큼 차이나는 길은 갈 수 있다고 생각하고 길을 다 구해
k만큼 지나는 길을 지나갈때는 카운트를 해
근데 카운트가 2를 넘어가면 그 길은 X
어차피 주변부터 시작이야
그러면 dfs를 써야겠네
"""