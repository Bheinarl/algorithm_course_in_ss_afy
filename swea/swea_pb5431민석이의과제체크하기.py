T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())
    ARR = list(map(int, input().split()))

    student = [0] * (N+1)
    ans = []

    for i in range(K):
        student[ARR[i]] = 1

    for j in range(1, N+1):
        if student[j] != 1:
            ans += [j]

    print(f'#{TEST_CASE}', end=' ')
    print(*ans, end=' ')
    print()
