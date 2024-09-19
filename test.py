import sys


def dfs(idx):
    global complete

    if complete == 1:  # 다 끝났는데 끝내주세요 시간초과 떠요
        return
    elif idx == N:  # 끝
        ans[:] = queen_lst[:]
        complete = 1
        return
    else:
        if queen_lst[idx] != 0:  # 이미 주어진 퀸은 고정
            if check(idx):
                dfs(idx + 1)
        else:
            for i in range(1, N + 1):
                # 지금까지는 괜찮다고 하면
                if not cols[i] and not diagonals19[idx - i] and not diagonals37[idx + i]:
                    # 퀸 배치
                    queen_lst[idx] = i
                    cols[i] = 1  # 열 check
                    diagonals19[idx - i] = 1  # 우상향 대각선 check
                    diagonals37[idx + i] = 1  # 우하향 대각선 check
                    if check(idx):  # 여기에 놓아도 괜찮을까요
                        dfs(idx + 1)  # 감사합니다
                    # 퀸 제거 (백트래킹)
                    queen_lst[idx] = 0  # 다시 짐 빼
                    cols[i] = 0
                    diagonals19[idx - i] = 0
                    diagonals37[idx + i] = 0


def check(idx):
    # 일단 당연히 같은 열, 행에는 있으면 안됨
    # 대각선은 저 'or' 뒤에처럼 차이로 판별 가능함
    for j in range(idx):
        if queen_lst[idx] == queen_lst[j] or abs(j - idx) == abs(queen_lst[j] - queen_lst[idx]):
            return 0
    return 1


N = int(sys.stdin.readline())
queen_lst = list(map(int, sys.stdin.readline().split()))
ans = [0] * N
complete = 0

# 열, 대각선 체크용 배열
cols = [0] * (N + 1)
diagonals19 = [0] * (2 * N)  # 우상향 대각선
diagonals37 = [0] * (2 * N)  # 우하향 대각선

# 미리 주어진 퀸의 위치를 설정
# 결국 보면 좌표의 차이와 합이 겹치는 게 없어야 N-Queen 조건에 부합
# 내가 했던 것과 다른 것은 아예 열과 두 방향의 대각선도 한 번에 체크하게 해준다는 점.
# 이걸로 시간이 확실히 단축되었다.
# 시간 초과 -> 176ms
for p in range(N):
    if queen_lst[p] != 0:
        q_col = queen_lst[p]
        cols[q_col] = 1
        diagonals19[p - q_col] = 1
        diagonals37[p + q_col] = 1

dfs(0)

if complete == 1:
    print(*ans)
else:
    print(-1)
