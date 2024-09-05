def f(i, cost):
    global min_cost

    if cost >= min_cost:
        return
    elif i == N:
        if min_cost > cost:
            min_cost = cost
    else:
        for j in range(N):
            if j not in path:
                path.append(j)
                f(i+1, cost + ARR[i][j])
                path.pop()


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    min_cost = 99 * N**2
    path = []
    f(0, 0)

    print(f'#{TEST_CASE} {min_cost}')