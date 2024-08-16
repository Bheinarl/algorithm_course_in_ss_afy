T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for i in range(N):
        ARR += [list(map(int, input().split()))]

    counts = 0
    for i in range(len(ARR)):
        [x, y] = ARR[i]
        for line in ARR:
            if x < line[0] and y > line[1]:
                counts += 1
            elif x > line[0] and y < line[1]:
                counts += 1

    # 100% 두 번 세었을거야
    real_counts = counts // 2
    print(f'#{TEST_CASE} {real_counts}')