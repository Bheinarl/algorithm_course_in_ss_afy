T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []  # 결과값을 담을 list

    for i in range(N):  # 안에 넣으면 Q번 돌아야해서 밖으로 뺐어요
        for j in range(N):
            if ARR[i][j] == 'X':
                si, sj = i, j

    for _ in range(Q):
        TEMP = list(input().split())
        C = int(TEMP[0])
        COMMAND = list(TEMP[1])

        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        d = 0

        ni, nj = si, sj

        # 명령어를 스캔해봅시다.
        for COMMAND_INDEX in range(C):
            if COMMAND[COMMAND_INDEX] == 'R':  # 시계방향 90도 회전
                d = (d + 1) % 4
            elif COMMAND[COMMAND_INDEX] == 'L':  # 반시계방향 90도 회전
                d = (d - 1) % 4
            elif COMMAND[COMMAND_INDEX] == 'A':  # 직진 그런데 조건을 곁들인
                temp_ni = ni + direction[d][0]  # 임시로 한 이유는 나무나 필드를 벗어나는 경우에는
                temp_nj = nj + direction[d][1]  # 아무일도 일어나지 않기 때문
                if 0 <= temp_ni < N and 0 <= temp_nj < N:
                    if ARR[temp_ni][temp_nj] != 'T':
                        ni, nj = temp_ni, temp_nj

        if ARR[ni][nj] == 'Y':  # 다 움직였을 때 도착지점에 있다면
            result.append(1)
        else:                   # 다 움직였을 때 도착지점에 없다면
            result.append(0)

    print(f'#{TEST_CASE}', end=' ')
    print(*result)