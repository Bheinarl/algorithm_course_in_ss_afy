def find_set(x):
    if rep[x] == x:
        return x

    rep[x] = find_set(rep[x])
    return rep[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    # 더 작은 루트노트에 합친다.
    if root_x < root_y:
        rep[root_y] = root_x
    else:
        rep[root_x] = root_y


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    edge = []
    rep = [u for u in range(N)]

    for i in range(0, N-1):
        for j in range(i+1, N):
            edge.append((i, j, (island_x[i] - island_x[j])**2 + (island_y[i] - island_y[j])**2))

    edge.sort(key=lambda x: x[2])

    edge_counts = 0
    ans = 0
    for s, e, money in edge:
        if find_set(s) != find_set(e):
            union(s, e)
            edge_counts += 1
            ans += money
        if edge_counts == N:
            break

    ans *= E
    ans = int(round(ans, 0))
    print(f'#{TEST_CASE} {ans}')
