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