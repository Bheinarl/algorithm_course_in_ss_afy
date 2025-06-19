def save_coordinate():  # 달팽이 순서대로 좌표 저장
    x, y = N//2, N//2
    length = 1
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌, 하, 우, 상
    coordinates = []
    while True:
        for d in dirs:
            for _ in range(length):
                x += d[0]
                y += d[1]
                if 0 <= x < N and 0 <= y < N:
                    coordinates.append((x, y))
                if x == 0 and y == 0:
                    return coordinates
            if d == dirs[1] or d == dirs[3]:
                length += 1

def board_to_marbles():  # 1차원 구슬로 변환
    return [board[x][y] for x, y in coordinates]

def marbles_to_board(marbles):  # 2차원 좌표 형식으로 변환
    for i, (x, y) in enumerate(coordinates):
        board[x][y] = marbles[i] if i < len(marbles) else 0  # marbles에 값이 있으면 그걸 쓰고 아니면 0

def blizzard(d, s):  # 구슬 파괴
    cx, cy = N//2, N//2
    for i in range(1, s+1):
        nx = cx + dx[d]*i
        ny = cy + dy[d]*i
        board[nx][ny] = 0

def move(marbles):  # 구슬 정렬
    return [b for b in marbles if b != 0]

def explode(marbles):  # 연속 구슬 BOOM
    new_marbles = []
    exploded = False
    i = 0
    while i < len(marbles):
        j = i
        while j < len(marbles) and marbles[j] == marbles[i]:
            j += 1
        if j - i >= 4:
            exploded = True
            score[marbles[i]] += j - i
        else:
            new_marbles.extend(marbles[i:j])
        i = j
    return new_marbles, exploded

def transform(marbles):  # 연속된 구슬 모아
    result = []
    i = 0
    while i < len(marbles):
        j = i
        while j < len(marbles) and marbles[j] == marbles[i]:
            j += 1
        count = j - i
        num = marbles[i]
        result.extend([count, num])
        i = j
    return result[:N*N - 1]


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [tuple(map(int, input().split())) for _ in range(M)]

coordinates = save_coordinate()

score = {1: 0, 2: 0, 3: 0}

for d, s in magic:
    # 블리자드로 파괴
    blizzard(d, s)

    # 2D → 1D 변환 및 이동
    marbles = move(board_to_marbles())

    # 폭발 반복
    while True:
        marbles, exploded = explode(marbles)
        if not exploded:
            break

    # 그룹 변환
    marbles = transform(marbles)

    # 다시 보드에 적용
    marbles_to_board(marbles)

print(score[1] * 1 + score[2] * 2 + score[3] * 3)