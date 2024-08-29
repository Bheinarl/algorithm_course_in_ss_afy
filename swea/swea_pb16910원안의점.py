T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    counts = 0

    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if i**2 + j**2 <= N**2:
                counts += 1

    print(f'#{TEST_CASE} {counts}')
