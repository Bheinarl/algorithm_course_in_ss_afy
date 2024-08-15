T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    num = [0] * 10
    counts = 1
    k = 1
    n = N
    while sum(num) < 10:
        N = str(N)
        for i in N:
            i = int(i)
            if num[i] == 0:
                num[i] = 1

        counts += 1

        N = n * counts

    print(f'#{TEST_CASE} {n*(counts-1)}')
