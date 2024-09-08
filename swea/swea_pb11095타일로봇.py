T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    visited = [[0]*10 for _ in range(10)]
    counts = 0

    for _ in range(N):
        i1, j1, i2, j2 = map(int, input().split())
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                visited[i][j] = 1

    for p in range(10):
        for q in range(10):
            if visited[p][q] != 0:
                counts += 1

    print(f'#{TEST_CASE} {counts}')