T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]
    min_counts = N*M
    for a in range(N-2):
        for b in range(a+1, N-1):
            counts = 0
            for j in range(M):
                for p in range(0, a+1):
                    if ARR[p][j] != 'W':
                        counts += 1
                for q in range(a+1, b+1):
                    if ARR[q][j] != 'B':
                        counts += 1
                for r in range(b+1, N):
                    if ARR[r][j] != 'R':
                        counts += 1

            if min_counts > counts:
                min_counts = counts

    print(f'#{TEST_CASE} {min_counts}')

"""
def f(a, b, c):
    global min_counts

    if a + b + c == N:
        counts = 0
        for j in range(M):
            for p in range(a):
                if ARR[p][j] != 'W':
                    counts += 1
            for q in range(a, a+b):
                if ARR[q][j] != 'B':
                    counts += 1
            for r in range(a+b, N):
                if ARR[r][j] != 'R':
                    counts += 1
        if min_counts > counts:
            min_counts = counts

    else:
        f(a+1, b, c)
        f(a, b+1, c)
        f(a, b, c+1)


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]
    min_counts = N*M

    f(1, 1, 1)

    print(f'#{TEST_CASE} {min_counts}')

"""

"""
def f():

    min_counts = N*M+1
    for a in range(N-2):
        for b in range(a+1, N-1):
            counts = 0
            for j in range(M):
                for x in range(0, a+1):
                    if ARR[x][j] != 'W':
                        counts += 1
                for y in range(a+1, b+1):
                    if ARR[y][j] != 'B':
                        counts += 1
                for z in range(b+1, N):
                    if ARR[z][j] != 'R':
                        counts += 1

            if min_counts > counts:
                min_counts = counts

    return min_counts


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
"""

"""
T = int(input())
for TEST_CASE in range(1, T+1):

    N, M = map(int, input().split())

    ARR = []

    for _ in range(N):
        ARR += [list(input())]

    min_counts = N*M  # 다 틀렸을 때가 나올 수 있는 최솟값의 최댓값

    for a in range(N-2):  # a는 N-2까지가 최대
        for b in range(a+1, N-1):  # b는 a 다음 숫자부터 N-1까지가 최대
            counts = 0             # c는 나머지
            for j in range(M):

                for x in range(a+1):  # 0 ~ a 범위만큼 스캔
                    if ARR[x][j] != 'W':
                        counts += 1

                for y in range(a+1,b+1):  # a+1 ~ b 범위만큼 스캔
                    if ARR[y][j] != 'B':
                        counts += 1

                for z in range(b+1,N):  # b+1 ~ N 범위만큼 스캔
                    if ARR[z][j] != 'R':
                        counts += 1

            if min_counts >= counts:
                min_counts = counts

    print(f'#{TEST_CASE} {min_counts}')
"""