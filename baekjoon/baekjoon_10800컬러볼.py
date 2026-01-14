import sys
input = sys.stdin.readline

N = int(input())
balls = []

for i in range(N):
    c, s = map(int, input().split())
    balls.append((i, c, s))  # (원래 인덱스, 색, 크기)

# 크기 기준 정렬
balls.sort(key=lambda x: x[2])

answer = [0] * N
color_sum = [0] * (N + 1)
total_sum = 0

i = 0
while i < N:
    j = i

    # 같은 크기 묶기
    while j < N and balls[i][2] == balls[j][2]:
        j += 1

    # 계산 먼저 (같은 크기는 제외해야 하니까)
    for k in range(i, j):
        idx, color, size = balls[k]
        answer[idx] = total_sum - color_sum[color]

    # 누적합 반영
    for k in range(i, j):
        idx, color, size = balls[k]
        total_sum += size
        color_sum[color] += size

    i = j

for v in answer:
    print(v)