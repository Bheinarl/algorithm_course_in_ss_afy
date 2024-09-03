T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]
    land = []
    water = []
    for i in range(N):
        for j in range(M):
            if ARR[i][j] == 'W':
                water += [[i, j]]
            else:
                land += [[i, j]]

    sum_ans = 0
    for a in range(len(land)):
        land_i = land[a][0]
        land_j = land[a][1]
        min_dist = 999999999999999999999
        for b in range(len(water)):
            water_i = water[b][0]
            water_j = water[b][1]
            dist = abs(land_i - water_i) + abs(land_j - water_j)
            if dist == 1:
                min_dist = 1
                break
            elif min_dist > dist:
                min_dist = dist
        sum_ans += min_dist

    print(f'#{TEST_CASE} {sum_ans}')
