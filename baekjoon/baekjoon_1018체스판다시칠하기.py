N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr += [list(input())]

min_counts = N*M
for p in range(N-7):
    for q in range(M-7):
        counts_B = 0
        counts_W = 0
        for i in range(p, p+8):
            for j in range(q, q+8):
                if i == p and j == q and arr[i][j] != 'B':
                    counts_B += 1
                elif ((i-p) % 2 + (j-q) % 2) % 2 == 0 and arr[i][j] != 'B':
                    counts_B += 1
                elif ((i-p) % 2 + (j-q) % 2) % 2 == 1 and arr[i][j] != 'W':
                    counts_B += 1

                if i == p and j == q and arr[i][j] != 'W':
                    counts_W += 1
                elif ((i-p) % 2 + (j-q) % 2) % 2 == 0 and arr[i][j] != 'W':
                    counts_W += 1
                elif ((i-p) % 2 + (j-q) % 2) % 2 == 1 and arr[i][j] != 'B':
                    counts_W += 1

        if min(counts_B, counts_W) < min_counts:
            min_counts = min(counts_B, counts_W)

print(min_counts)
