def f(stop, battery, counts):
    global min_counts

    if counts >= min_counts:
        return
    elif stop >= N-1:
        if counts < min_counts:
            min_counts = counts
    else:
        for i in range(stop + 1, stop + battery + 1):
            if i <= N-1:
                f(i, BTR[i], counts+1)


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(map(int, input().split()))
    N = ARR[0]
    BTR = ARR[1:] + [0]
    min_counts = N+1
    f(0, BTR[0], -1)

    print(f'#{TEST_CASE} {min_counts}')
