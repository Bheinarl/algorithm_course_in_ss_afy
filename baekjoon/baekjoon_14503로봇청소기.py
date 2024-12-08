N, M = map(int, input().split())  # 2차원 리스트 크기
r, c, d = map(int, input().split())  # 시작 지점과 방향
LST = [list(map(int, input().split())) for _ in range(N)]  # 2차원 리스트(작업판)

ni, nj = r, c  # 알아보기 쉽게 변수 변경
ans = 0  # 청소 횟수

# 북 동 남 서 방향(시계방향)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


while True:
    if ni < 0 or ni >= N or nj < 0 or nj >= M or LST[ni][nj] == 1:
        # 2. 바라보는 방향의 뒤쪽 칸이 범위를 넘어서거나 벽이여서 후진을 할 수 없자면
        break  # 작동을 멈춘다.
    elif LST[ni][nj] == 0:  # 1. 현재 자리가 청소되지 않았다면
        LST[ni][nj] = 2  # 현재 칸을 청소한다. (청소가 된 칸은 2로 표시)
        ans += 1  # 청소 횟수 표시
    else:  # 현재 자리가 청소가 되었다면
        for _ in range(4):  # 회전을 할꺼야
            d = (d - 1) % 4  # 반시계방향으로
            if 0 <= ni + di[d] < N and 0 <= nj + dj[d] < M and LST[ni + di[d]][nj + dj[d]] == 0:
                # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우(0이 있는 경우)
                ni = ni + di[d]  # 바라보는 방향으로 한 칸 전진한다.
                nj = nj + dj[d]
                break  # 1번으로 돌아간다.
        else:  # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
            ni = ni - di[d]  # 한 칸 후진하고
            nj = nj - dj[d]  # 1번으로 돌아간다.

print(ans)

