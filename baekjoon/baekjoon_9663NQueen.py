n = int(input())
ans = 0

cols = [False] * n               # 세로(열) 충돌 체크
diagonalL2R = [False] * (2 * n - 1)    # 좌상 -> 우하 대각선 r+c
diagonalR2L = [False] * (2 * n - 1)    # 우상 -> 좌하 대각선 r-c+n-1

def dfs(r):
    global ans
    if r == n:       # 모든 행에 퀸을 배치했으면 경우의 수 +1
        ans += 1
        return
    for c in range(n):
        if cols[c] or diagonalL2R[r + c] or diagonalR2L[r - c + (n - 1)]:
            continue
        cols[c] = diagonalL2R[r + c] = diagonalR2L[r - c + (n - 1)] = True
        dfs(r + 1)
        cols[c] = diagonalL2R[r + c] = diagonalR2L[r - c + (n - 1)] = False

dfs(0)
print(ans)