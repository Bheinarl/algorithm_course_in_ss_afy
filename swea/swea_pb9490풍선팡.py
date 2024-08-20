def f():

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    max_pop = 0
    for i in range(N):
        for j in range(M):
            pop_time = ARR[i][j]
            pop_sum = 0
            for k in range(4):
                now_i = i
                now_j = j
                for z in range(pop_time+1):
                    if 0 <= now_i < N and 0 <= now_j < M:
                        pop_sum += ARR[now_i][now_j]
                        now_i += di[k]
                        now_j += dj[k]
            pop_sum -= 3* ARR[i][j]

            if max_pop < pop_sum:
                max_pop = pop_sum

    return max_pop


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')

"""
def func(n, m, arr):

    max_pop_counts = 0
    for i in range(n):
        # pop_counts = 0
        for j in range(m):
            pop_counts = 0
            pop_num = arr[i][j]
            pop_counts += arr[i][j]
            if i < pop_num:
                for k in range(i):
                    pop_counts += arr[k][j]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i-k][j]

            if i + pop_num >= n-1:
                for k in range(1, n-i):
                    pop_counts += arr[n-k][j]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i+k][j]

            if j <= pop_num:
                for k in range(j):
                    pop_counts += arr[i][k]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i][j-k]

            if j + pop_num >= m-1:
                for k in range(1, m-j):
                    pop_counts += arr[i][m-k]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i][j+k]

            if pop_counts >= max_pop_counts:
                max_pop_counts = pop_counts

    return max_pop_counts


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = func(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')
"""