T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    for i in range(N):
        ARR[i] = abs(ARR[i])

    min_dist = min(ARR)

    counts = 0
    for j in range(N):
        if ARR[j] == min_dist:
            counts += 1

    print(f'#{TEST_CASE} {min_dist} {counts}')
