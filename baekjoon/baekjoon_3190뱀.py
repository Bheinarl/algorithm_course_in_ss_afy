import sys
from collections import deque


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
list_apple = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
change_direction = [list(sys.stdin.readline().split()) for _ in range(L)]

for cd in change_direction:
    cd[0] = int(cd[0])

for apple in list_apple:
    apple[0] -= 1
    apple[1] -= 1

list_direction = [(0,1), (1,0), (0, -1), (-1,0)]  # 우하좌상 시계방향 // d+1 -> 오른쪽 회전 // d-1 -> 왼쪽 회전

snake = deque()
snake.append((0, 0))
now_direction = 0  # 갈 방향을 알려주는 index 번호
sec = 0

# 최대한 보드를 써보지 말아봅시다

while snake:
    ni, nj = snake.pop()  # 다음 갈 곳을 알아야하니깐 머리를 꺼냄
    snake.append((ni, nj))  # 정보는 얻었으니깐 머리 다시 집어넣음

    # 다음 머리가 갈 좌표
    ni += list_direction[now_direction][0]
    nj += list_direction[now_direction][1]

    sec += 1

    # 중단 조건 1. 몸통에 부딫힐 경우
    if (ni, nj) in snake:
        break

    # 중단 조건 2. 벽에 부딫힐 경우
    if 0 > ni or ni >= N or 0 > nj or nj >= N:
        break

    # 머리가 다음 좌표로 갈 수 있으므로 큐에 저장
    snake.append((ni, nj))

    # 사과를 먹지 않으면 꼬리가 앞으로 당겨짐 // 먹으면 꼬리는 그대로 가만히 있음
    if [ni, nj] not in list_apple:
        snake.popleft()

    # 먹은 사과는 지움
    if [ni, nj] in list_apple:
        list_apple.remove([ni, nj])

    # 방향을 바꿔야할 경우 방향을 전환
    for cd in change_direction:
        if sec in cd:
            if cd[1] == 'D':
                now_direction = (now_direction + 1) % 4
                break
            else:
                now_direction = (now_direction - 1) % 4
                break

print(sec)