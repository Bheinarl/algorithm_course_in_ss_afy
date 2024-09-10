def find_set(x):

    while rep[x] != x:
        x = rep[x]

    return x


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    rep = [n for n in range(N+1)]

    for i in range(M):
        n1, n2 = map(int, input().split())
        rep[find_set(n1)] = find_set(n2)

    counts = 0
    for j in range(1, N+1):
        if rep[j] == j:
            counts += 1

    print(f'#{TEST_CASE} {counts}')
