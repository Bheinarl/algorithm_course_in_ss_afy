T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    edge = []
    for i in range(1, N):
        for j in range(i, N+1):
            edge.append((i, j, (island_x[i] - island_x[j])**2 + (island_y[i] - island_y[j])**2 * L))