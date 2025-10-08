"""
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]

# 첫 번째 행 - 오른쪽으로만 탐사할 수 있음
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + board[0][j]

# 두 번째 행 ~ 마지막 행
for i in range(1, N):
    left_2_right = [0] * M
    right_2_left = [0] * M

    # 왼쪽에서 오른쪽으로 탐사
    left_2_right[0] = dp[i - 1][0] + board[i][0]
    for j in range(1, M):
        left_2_right[j] = max(left_2_right[j - 1], dp[i - 1][j]) + board[i][j]

    # 오른쪽에서 왼쪽으로 탐사
    right_2_left[M - 1] = dp[i - 1][M - 1] + board[i][M - 1]
    for j in range(M - 2, -1, -1):
        right_2_left[j] = max(right_2_left[j + 1], dp[i - 1][j]) + board[i][j]

    # 두개 중에 더 큰 값
    for j in range(M):
        dp[i][j] = max(left_2_right[j], right_2_left[j])

print(dp[N - 1][M - 1])

"""

# ---

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 첫번째 줄 (똑같이 오른쪽으로만 탐사 가능)
dp = [0] * M
dp[0] = board[0][0]
for j in range(1, M):
    dp[j] = dp[j - 1] + board[0][j]

# 그 이후
for i in range(1, N):
    row = board[i]
    L2R = [0] * M
    R2L = [0] * M

    L2R[0] = dp[0] + row[0]
    for j in range(1, M):
        L2R[j] = max(L2R[j - 1], dp[j]) + row[j]

    R2L[M - 1] = dp[M - 1] + row[M - 1]
    for j in range(M - 2, -1, -1):
        R2L[j] = max(R2L[j + 1], dp[j]) + row[j]

    for j in range(M):
        dp[j] = max(L2R[j], R2L[j])

print(dp[M - 1])