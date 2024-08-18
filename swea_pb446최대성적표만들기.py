T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())
    ARR = list(map(int, input().split()))

    ARR.sort(reverse=True)

    max_score = 0

    for i in range(K):
        max_score += ARR[i]

    print(f'#{TEST_CASE} {max_score}')