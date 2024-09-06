def f(idx, sum_num):

    global counts

    if sum_num > K:
        return
    elif sum_num == K:
        counts += 1
    elif idx == N:
        return
    else:
        f(idx + 1, sum_num + ARR[idx])
        f(idx + 1, sum_num)


T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())
    ARR = list(map(int, input().split()))

    counts = 0
    f(0, 0)

    print(f'#{TEST_CASE} {counts}')
