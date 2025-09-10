import sys
input = sys.stdin.readline

green = [[0]*4 for _ in range(6)]
blue  = [[0]*6 for _ in range(4)]

def drop_green(t, x, y):
    if t == 1:  # 한 칸짜리 블록
        r = 0
        while r+1 < 6 and green[r+1][y] == 0:
            r += 1
        green[r][y] = 1
    elif t == 2:  # 가로 블록
        r = 0
        while r+1 < 6 and green[r+1][y] == 0 and green[r+1][y+1] == 0:
            r += 1
        green[r][y] = 1
        green[r][y+1] = 1
    else:  # 세로 블록
        r = 1  # 위 블록이 한 칸 위에 있으니까
        c = y
        # 아래가 0이면 내려
        while True:
            nr = r + 1
            up = nr - 1
            if nr < 6 and green[nr][c] == 0:
                r = nr
            else:
                break
        green[r][c] = 1
        green[r-1][c] = 1


def drop_blue(t, x, y):

    if t == 1:  # 한 칸짜리 블록
        c = 0
        while c+1 < 6 and blue[x][c+1] == 0:
            c += 1
        blue[x][c] = 1
    elif t == 2:  # 가로 블록
        c = 1
        while True:
            nc = c + 1
            if nc < 6 and blue[x][nc] == 0 and blue[x][nc-1] == 0:
                c = nc
            else:
                break
        blue[x][c] = 1
        blue[x][c-1] = 1
    else:  # 세로 블록
        c = 0
        r1, r2 = x, x+1
        while c+1 < 6 and blue[r1][c+1] == 0 and blue[r2][c+1] == 0:
            c += 1
        blue[r1][c] = 1
        blue[r2][c] = 1

def score_clear_green():
    # 초록판에서 가득 찬 가로줄 제거 및 점수 계산. 제거 후 위에서 아래로 떨어짐
    score = 0
    # 가득 찬 가로 줄 확인
    for r in range(5, 1, -1):
        if all(green[r][c] == 1 for c in range(4)):
            score += 1
            # 윗줄들을 한 칸씩 내림
            for rr in range(r, 0, -1):
                for cc in range(4):
                    green[rr][cc] = green[rr-1][cc]
            for cc in range(4):
                green[0][cc] = 0
            return score + score_clear_green()
    return score

def score_clear_blue():
    # 파랑판에서 가득 찬 세로줄 제거 및 점수 계산. 제거 후 좌에서 우로 떨어짐
    # 가득 찬 세로 줄 확인
    score = 0
    for c in range(5, 1, -1):
        full = True
        for r in range(4):
            if blue[r][c] == 0:
                full = False
                break
        if full:
            score += 1
            # 오른쪽에서 왼쪽으로 당김
            for cc in range(c, 0, -1):
                for rr in range(4):
                    blue[rr][cc] = blue[rr][cc-1]
            for rr in range(4):
                blue[rr][0] = 0
            return score + score_clear_blue()
    return score

def light_green():
    # 연두색 칸 처리: 존재하는 행 수만큼 맨 아래 없애고 전체 아래로 밀기
    cnt = 0
    for r in [0, 1]:
        if any(green[r][c] == 1 for c in range(4)):
            cnt += 1
    for _ in range(cnt):
        # 맨 아래 행 제거
        for c in range(4):
            green[5][c] = 0
        # 위에서 아래로 모두 한 칸씩 밀기
        for r in range(5, 0, -1):
            for c in range(4):
                green[r][c] = green[r-1][c]
        for c in range(4):
            green[0][c] = 0

def skyblue():
    # 하늘색 칸 처리: 존재하는 열 수만큼 맨 오른쪽 없애고 전체 오른쪽으로 밀기
    cnt = 0
    for c in [0, 1]:
        if any(blue[r][c] == 1 for r in range(4)):
            cnt += 1
    for _ in range(cnt):
        # 맨 오른쪽 열 제거
        for r in range(4):
            blue[r][5] = 0
        # 오른쪽으로 한 칸씩 밀기
        for c in range(5, 0, -1):
            for r in range(4):
                blue[r][c] = blue[r][c-1]
        for r in range(4):
            blue[r][0] = 0

def count_blocks():
    s = 0
    for r in range(6):
        for c in range(4):
            s += green[r][c]
    for r in range(4):
        for c in range(6):
            s += blue[r][c]
    return s

N = int(input())
score = 0
for _ in range(N):
    t, x, y = map(int, input().split())

    # 초록판
    if t == 1:
        drop_green(1, x, y)
    elif t == 2:
        drop_green(2, x, y)
    else:
        drop_green(3, x, y)

    # 파랑판
    if t == 1:
        drop_blue(1, x, y)
    elif t == 2:
        drop_blue(2, x, y)
    else:
        drop_blue(3, x, y)

    # 가득 찬 줄 제거 및 점수 기록
    score += score_clear_green()
    score += score_clear_blue()

    # 연두색, 하늘색
    light_green()
    skyblue()

print(score)
print(count_blocks())
