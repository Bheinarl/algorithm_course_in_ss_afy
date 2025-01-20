from itertools import combinations

def check_same_num():
    for start_num in range(N):  # 세로선
        vertical_line = start_num
        for horizontal_line in range(H):  # 가로선(이 있는 좌표같은 거)
            if ladders[horizontal_line][vertical_line]:  #  정방향
                vertical_line += 1
            elif ladders[horizontal_line][vertical_line - 1]:  # 역방향
                vertical_line -= 1
        if vertical_line != start_num:  # 다 했는데 시작점과 종료 위치가 다르면
            return False
    return True


N, M, H = map(int, input().split())
ladders = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = 1  # 1부터 시작하므로 index 값은 1 빼준 값부터 시작

if check_same_num():
    print(0)
    exit()

able2draw = []
for i in range(H):
    for j in range(N - 1):  # N번째 세로선은 오른쪽으로 그리지 못함
        if ladders[i][j] == 0 and (j == 0 or ladders[i][j-1] == 0) and ladders[i][j+1] == 0:  # 가로선이 양 옆에 없어야 그릴 수 있다.
            able2draw.append((i, j))

for new_line in range(1, 4):
    for combination in combinations(able2draw, new_line):
        for i, j in combination:  # 새로운 선을 그려
            ladders[i][j] = 1
        if check_same_num():  # 확인을 해
            print(new_line)
            exit()
        for i, j in combination:  # 안될 경우 다시 초기화
            ladders[i][j] = 0

    new_line += 1

print(-1)  # 다 했는데도 안되면 -1 출력