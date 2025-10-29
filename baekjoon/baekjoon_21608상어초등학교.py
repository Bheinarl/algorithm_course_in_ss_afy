import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def in_range(n, i, j):
    return 0 <= i < n and 0 <= j < n

def find_seat(n, board, likes, student):

    """
    우선 순위(문제 내용)
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    """

    best_like = -1
    best_empty = -1
    best_i, best_j = n, n

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue

            like_count = 0
            empty_count = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if not in_range(n, ni, nj):
                    continue
                if board[ni][nj] == 0:
                    empty_count += 1
                elif board[ni][nj] in likes[student]:
                    like_count += 1

            # 좋아하는 학생 수가 더 많으면 갱신
            if like_count > best_like:
                best_like, best_empty, best_i, best_j = like_count, empty_count, i, j
            # 좋아하는 학생 수가 같다면, 빈칸이 더 많은 곳
            elif like_count == best_like and empty_count > best_empty:
                best_empty, best_i, best_j = empty_count, i, j
            # 빈 칸 수가 같다면, 행 번호가 더 작은 곳
            elif like_count == best_like and empty_count == best_empty and i < best_i:
                best_i, best_j = i, j
            # 행 번호도 같다면, 열 번호가 더 작은 곳
            elif like_count == best_like and empty_count == best_empty and i == best_i and j < best_j:
                best_j = j

    board[best_i][best_j] = student

def total_satisfaction(n, board, likes):
    satisfaction_map = [0, 1, 10, 100, 1000]
    total = 0
    for i in range(n):
        for j in range(n):
            s = board[i][j]
            counts = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if in_range(n, ni, nj) and board[ni][nj] in likes[s]:
                    counts += 1
            total += satisfaction_map[counts]
    return total


N = int(input())
board = [[0] * N for _ in range(N)]
likes = dict()
order = []

for _ in range(N * N):
    a, b, c, d, e = map(int, input().split())
    likes[a] = {b, c, d, e}
    order.append(a)

for s in order:
    find_seat(N, board, likes, s)

print(total_satisfaction(N, board, likes))