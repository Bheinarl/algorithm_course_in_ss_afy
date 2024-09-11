def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(a, b):
    rep[find_set(b)] = find_set(a)


T = int(input())
for TEST_CASE in range(1, T+1):
    V, E = map(int, input().split())

    rep = [u for u in range(V+1)]

    edge = [list(map(int, input().split())) for _ in range(E)]

    edge.sort(key=lambda x: x[2])

    edge_counts = 0

    ans = 0

    for s, e, value in edge:
        if find_set(s) != find_set(e):
            union(s, e)
            edge_counts += 1
            ans += value
        if edge_counts == V:
            break

    print(f'#{TEST_CASE} {ans}')
