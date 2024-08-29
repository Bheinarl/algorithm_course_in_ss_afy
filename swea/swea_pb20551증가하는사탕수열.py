T = int(input())
for TEST_CASE in range(1, T+1):
    A, B, C = map(int, input().split())

    counts = 0
    if B >= C:
        counts += B-C+1
        B = C-1

    if A >= B:
        counts += A-B+1
        A = B-1

    if A <= 0:
        counts = -1

    print(f'#{TEST_CASE} {counts}')
