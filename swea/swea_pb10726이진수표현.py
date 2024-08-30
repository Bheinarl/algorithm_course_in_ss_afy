T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    counts = 0

    for i in range(N):
        if M & (1 << i):
            counts += 1

    if counts == N:
        print(f'#{TEST_CASE} ON')
    else:
        print(f'#{TEST_CASE} OFF')
