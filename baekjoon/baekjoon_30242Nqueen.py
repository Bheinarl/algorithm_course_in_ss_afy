import sys


def check(idx):
    for j in range(idx):
        if queen_lst[idx] == queen_lst[j] or abs(j - idx) == abs(queen_lst[j] - queen_lst[idx]):
            return 0

    return 1


def dfs(idx):
    global ans
    global complete

    if complete == 1:
        return
    elif idx == N:
        ans = queen_lst[:]
        complete = 1
    else:
        if queen_lst[idx] == 0:
            for i in range(1, N+1):
                queen_lst[idx] = i
                if check(idx):
                    dfs(idx+1)
                queen_lst[idx] = 0
        else:
            if check(idx):
                dfs(idx+1)


N = int(sys.stdin.readline())
queen_lst = list(map(int, sys.stdin.readline().split()))
ans = []
complete = 0
dfs(0)
if len(ans) == 0:
    print(-1)
else:
    print(*ans)