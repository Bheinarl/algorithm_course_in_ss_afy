def f():

    di_2468 = [1, 0, 0, -1]
    dj_2468 = [0, -1, 1, 0]

    di_1379 = [1, 1, -1, -1]
    dj_1379 = [-1, 1, -1, 1]

    fly_max = 0
    for i in range(N):
        for j in range(N):
            fly_2468 = 0
            fly_1379 = 0

            for k in range(4):
                now_i = i
                now_j = j
                for _ in range(M):
                    if 0 <= now_i < N and 0 <= now_j < N:
                        fly_2468 += ARR[now_i][now_j]
                        now_i += di_2468[k]
                        now_j += dj_2468[k]

            for k in range(4):
                now_i = i
                now_j = j
                for _ in range(M):
                    if 0 <= now_i < N and 0 <= now_j < N:
                        fly_1379 += ARR[now_i][now_j]
                        now_i += di_1379[k]
                        now_j += dj_1379[k]

            fly_2468 -= ARR[i][j] * 3
            fly_1379 -= ARR[i][j] * 3

            if fly_max < max(fly_2468, fly_1379):
                fly_max = max(fly_2468, fly_1379)

    return fly_max


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
