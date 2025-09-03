import sys
input = sys.stdin.readline

def can_walk(line, L):
    n = len(line)
    used = [False] * n  # 경사로가 놓인 칸 표시

    i = 0
    while i < n - 1:
        current_floor, next_floor = line[i], line[i+1]
        if current_floor == next_floor:
            i += 1
            continue

        diff = next_floor - current_floor
        # 높이 차가 2 이상이면 안됨
        if abs(diff) > 1:
            return False

        if diff == -1:
            # 내리막: i+1부터 L칸이 next_floor와 모두 같아야 함
            for j in range(i+1, i+1+L):
                if j >= n or line[j] != next_floor or used[j]:
                    return False
            for j in range(i+1, i+1+L):
                used[j] = True
            i += 1
        else:
            # 오르막: i-L+1부터 i까지 L칸이 current_floor와 모두 같아야 함
            for j in range(i, i-L, -1):
                if j < 0 or line[j] != current_floor or used[j]:
                    return False
            for j in range(i, i-L, -1):
                used[j] = True
            i += 1
    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for r in range(N):
    if can_walk(board[r], L):
        ans += 1

for c in range(N):
    col = [board[r][c] for r in range(N)]
    if can_walk(col, L):
        ans += 1

print(ans)