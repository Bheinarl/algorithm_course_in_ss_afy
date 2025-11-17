import sys
input = sys.stdin.readline

def length_from_char(char):
    if 'a' <= char <= 'z':
        return ord(char) - 97 + 1  # ord('a') = 97
    if 'A' <= char <= 'Z':
        return ord(char) - 65 + 27  # ord('A') = 65
    return 0


INF = float('inf')

N = int(input().strip())

# i와 j 사이 최소 케이블 길이
cost = [[INF] * N for _ in range(N)]

total_len = 0

for i in range(N):
    len_line = input().strip()
    for j, char in enumerate(len_line):
        weight = length_from_char(char)
        if weight > 0:

            total_len += weight

            if weight < cost[i][j]:
                cost[i][j] = weight
                cost[j][i] = weight  # 양방향

# 프림 알고리즘
visited = [False] * N
distants = [INF] * N

# 어디서 시작해도 똑같음
distants[0] = 0
mst_len = 0

for _ in range(N):
    u = -1
    min_w = INF
    # 아직 방문 안 한 것 중 최소치
    for v in range(N):
        if not visited[v] and distants[v] < min_w:
            min_w = distants[v]
            u = v

    # 더 이상 갈 곳이 없다는 것은 다 연결되지 않는다는 것
    if u == -1:
        print(-1)
        sys.exit(0)

    visited[u] = True
    mst_len += distants[u]

    # u에서 갈 수 있는 이웃 정점들의 distants 갱신
    for v in range(N):
        if not visited[v] and cost[u][v] < distants[v]:
            distants[v] = cost[u][v]

# 다 돌아갔으면 다 연결됐다는 것
print(total_len - mst_len)