import sys
from collections import deque
input = sys.stdin.readline

def rotate_circles(x, d, k):
    rotation_direction = k if d == 0 else -k
    for i in range(x - 1, N, x):
        circles[i].rotate(rotation_direction)

def remove_same():
    is_removed = False
    # 동시에 지워야하므로 지울지만 표시 후 동시에 지움
    temp = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            num = circles[i][j]
            if num == 0:
                continue

            # 같은 원판 양 옆
            left_j = (j - 1) % M
            right_j = (j + 1) % M
            if circles[i][left_j] == num:
                temp[i][j] = temp[i][left_j] = True
            if circles[i][right_j] == num:
                temp[i][j] = temp[i][right_j] = True

            # 인접한 다른 원판과 비교
            if i - 1 >= 0 and circles[i - 1][j] == num:
                temp[i][j] = temp[i - 1][j] = True
            if i + 1 < N and circles[i + 1][j] == num:
                temp[i][j] = temp[i + 1][j] = True

    # 표시한 거 지우기
    for i in range(N):
        for j in range(M):
            if temp[i][j]:
                circles[i][j] = 0
                is_removed = True

    return is_removed

def calculate_with_average():
    total = 0
    counts = 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                total += circles[i][j]
                counts += 1

    if counts == 0:
        return

    avg = total / counts
    for i in range(N):
        for j in range(M):
            v = circles[i][j]
            if v == 0:
                continue
            if v > avg:
                circles[i][j] = v - 1
            elif v < avg:
                circles[i][j] = v + 1


N, M, T = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    rotate_circles(x, d, k)
    is_removed = remove_same()
    if not is_removed:
        calculate_with_average()

answer = 0
for i in range(N):
    answer += sum(circles[i])
print(answer)