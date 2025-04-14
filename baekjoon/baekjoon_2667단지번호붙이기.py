from collections import deque

def bfs(i, j):

    danji = 0

    Q = deque()
    Q.append((i, j))
    while Q:
        ni, nj = Q.popleft()
        APT[ni][nj] = '0'
        danji += 1
        for k in range(4):
            if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N:
                if APT[ni + di[k]][nj + dj[k]] == '1':
                    Q.append((ni + di[k], nj + dj[k]))
                    APT[ni + di[k]][nj + dj[k]] = '0'
    return danji


N = int(input())

APT = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans_list = []

for p in range(N):
    for q in range(N):
        if APT[p][q] == '1':
            house_num = bfs(p, q)
            ans_list.append(house_num)

ans_list.sort()
print(len(ans_list))
for n in range(len(ans_list)):
    print(ans_list[n])