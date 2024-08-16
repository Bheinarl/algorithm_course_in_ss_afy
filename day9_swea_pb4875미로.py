def find_start_end_point(arr, n):  # 출발점과 목적지 검색 함수
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                sp = [i, j]
            elif arr[i][j] == 3:
                ep = [i, j]
    return sp, ep


def dfs(sp, ep):
    now_i = sp[0]  # 현재 위치를 출발점으로 설정
    now_j = sp[1]
    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    visited2[now_i][now_j] = 1
    stack = []
    k = 0

    while True:
        if [now_i, now_j] == ep:  # 현재 위치가 목적지면 함수 종료, 1 반환
            return 1

        for k in range(4):  # 4방향을 스캔해주면서
            if 0 <= now_i+di[k] < N and 0 <= now_j+dj[k] < N and ARR[now_i+di[k]][now_j+dj[k]] != 1 and visited2[now_i+di[k]][now_j+dj[k]]==0:
                # 다음 좌표가 인덱스를 넘어가지 않거나, 벽이 아니거나, 이미 갔던 곳이 아니라면
                stack += [[now_i, now_j]]  # 현재 위치를 stack 에 저장하고
                now_i += di[k]  # 위치를 이동
                now_j += dj[k]
                visited2[now_i][now_j] = 1  # 간 적 있다고 표시
                break  # for 구문 break
        else:  # 네 방향을 다 봤는데 갈 곳이 없다면
            if stack:  # stack 이 존재한다면
                [now_i, now_j] = stack.pop()  # 현재 위치를 이전 위치로 이동
            else:  # stack 이 비어있다면
                return 0  # 갈 수 없다면 함수 종료, 0 반환


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    for i in range(N):
        for j in range(N):
            ARR[i][j] = int(ARR[i][j])

    SP, EP = find_start_end_point(ARR, N)

    # 방향을 우, 상, 좌, 하 순서로 설정
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    result = dfs(SP, EP)

    print(f'#{test_case} {result}')