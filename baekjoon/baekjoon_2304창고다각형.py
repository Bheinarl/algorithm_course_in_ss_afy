N = int(input())
ARR_x = []
ARR_y = []
for _ in range(N):
    x, y = map(int, input().split())
    ARR_x += [x]
    ARR_y += [y]

max_hei = max(ARR_y)

for k in range(N):
    if ARR_y[k] == max_hei:
        max_idx = k

sp = min(ARR_x)
ep = min(ARR_x)
area = 0

for i in range(sp, max_idx):
    if i == sp:
        area += ARR_x[]