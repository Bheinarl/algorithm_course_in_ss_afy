import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

answer = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        blocked = False

        # i < j 인 경우
        if i < j:
            for k in range(i + 1, j):
                # i <-> j 직선의 k 위치 높이
                y = H[i] + (H[j] - H[i]) * (k - i) / (j - i)
                if H[k] >= y:
                    blocked = True
                    break

        # i > j 인 경우
        else:
            for k in range(j + 1, i):
                y = H[i] + (H[j] - H[i]) * (k - i) / (j - i)
                if H[k] >= y:
                    blocked = True
                    break

        if not blocked:
            cnt += 1

    answer = max(answer, cnt)

print(answer)