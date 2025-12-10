import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs_taxi_to_passenger(n, board, taxi_i, taxi_j, sonnims):

    goal = [[-1] * n for _ in range(n)]
    q = deque()
    goal[taxi_i][taxi_j] = 0
    q.append((taxi_i, taxi_j))

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if board[ni][nj] == 1:
                continue
            if goal[ni][nj] != -1:
                continue
            goal[ni][nj] = goal[i][j] + 1
            q.append((ni, nj))

    best_start_i, best_start_j = -1, -1
    best_goal = -1

    for (start_i, start_j) in sonnims.keys():
        g = goal[start_i][start_j]
        if g == -1:
            continue

        if best_goal == -1 or g < best_goal:
            best_goal = g
            best_start_i, best_start_j = start_i, start_j
        elif g == best_goal:
            if start_i < best_start_i or (start_i == best_start_i and start_j < best_start_j):
                best_start_i, best_start_j = start_i, start_j

    if best_goal == -1:
        return -1, -1, -1

    return best_start_i, best_start_j, best_goal


def bfs_passenger_to_goal(n, board, start_i, start_j, end_i, end_j):

    goal = [[-1] * n for _ in range(n)]
    q = deque()
    goal[start_i][start_j] = 0
    q.append((start_i, start_j))

    while q:
        i, j = q.popleft()

        if i == end_i and j == end_j:
            return goal[i][j]

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if board[ni][nj] == 1:
                continue
            if goal[ni][nj] != -1:
                continue
            goal[ni][nj] = goal[i][j] + 1
            q.append((ni, nj))

    return -1


N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1
taxi_j -= 1

sonnims = {}  # {(start_i, start_j) : (end_i, end_j)}
for _ in range(M):
    start_i, start_j, end_i, end_j = map(int, input().split())
    sonnims[(start_i - 1, start_j - 1)] = (end_i - 1, end_j - 1)

for _ in range(M):
    # 택시 -> 손님
    start_i, start_j, goal_to_start = bfs_taxi_to_passenger(
        N, board, taxi_i, taxi_j, sonnims
    )

    if goal_to_start == -1 or goal_to_start > fuel:
        print(-1)
        sys.exit(0)

    fuel -= goal_to_start
    taxi_i, taxi_j = start_i, start_j

    # 손님 -> 목적지
    end_i, end_j = sonnims[(start_i, start_j)]
    goal_to_end = bfs_passenger_to_goal(
        N, board, start_i, start_j, end_i, end_j
    )

    if goal_to_end == -1 or goal_to_end > fuel:
        print(-1)
        sys.exit(0)

    fuel -= goal_to_end
    fuel += goal_to_end * 2  # 연료 충전 보너스

    taxi_i, taxi_j = end_i, end_j

    del sonnims[(start_i, start_j)]

print(fuel)