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

"""
T = int(input())
for TEST_CASE in range(1, 1+T):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    dir_x2486 = [1, 0, -1, 0]
    dir_y2486 = [0, -1, 0, 1]
    dir_x1793 = [-1, -1, 1, 1]
    dir_y1793 = [-1, 1, 1, -1]

    max_sum = 0

    for i in range(N):
        for j in range(N):
            sum_1793 = ARR[i][j]
            sum_2486 = ARR[i][j]
            for k in range(4):
                ni_2486 = i
                nj_2486 = j
                ni_1793 = i
                nj_1793 = j
                for h in range(1, M):
                    ni_2486 = ni_2486 + dir_x2486[k]
                    nj_2486 = nj_2486 + dir_y2486[k]
                    ni_1793 = ni_1793 + dir_x1793[k]
                    nj_1793 = nj_1793 + dir_y1793[k]
                    if 0 <= ni_2486 < N and 0 <= nj_2486 < N:
                        sum_2486 += ARR[ni_2486][nj_2486]

                    if 0 <= ni_1793 < N and 0 <= nj_1793 < N:
                        sum_1793 += ARR[ni_1793][nj_1793]

            if max_sum < max(sum_1793, sum_2486):
                max_sum = max(sum_2486, sum_1793)

    print(f'#{TEST_CASE} {max_sum}')

"""