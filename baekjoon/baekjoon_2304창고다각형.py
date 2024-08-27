N = int(input())
ARR = []
for _ in range(N):
    x, y = map(int, input().split())
    ARR += [[x, y]]

max_height = 0
max_idx = 0
ARR.sort()

for q in range(N):
    if ARR[q][1] > max_height:
        max_height = ARR[q][1]
        max_idx = q

area = 0
height = ARR[0][1]
for i in range(1, max_idx + 1):
    area += (ARR[i][0] - ARR[i-1][0]) * height
    if ARR[i][1] > height:
        height = ARR[i][1]

area += max_height

height = ARR[-1][1]
for j in range(N-2, max_idx-1, -1):
    area += (ARR[j+1][0] - ARR[j][0]) * height
    if ARR[j][1] > height:
        height = ARR[j][1]

print(area)
