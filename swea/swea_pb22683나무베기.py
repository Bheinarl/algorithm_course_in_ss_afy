def dfs(ni, nj, d, cutting, counts):  # ni, nj : 현재 내가 있는 좌표, d : 현재 내 방향, cutting : 나무 자른 횟수, counts : 조작 횟수

    global min_control

    # 가지치기
    if counts >= min_control:  # 이미 앞서 구한 최솟값보다 더 많이 조작했으면 싹둑
        return
    elif ARR[ni][nj] == 'Y':  # 이동한 곳이 도착지면 이제 최소 값인지를 파악해줘요
        if counts < min_control:
            min_control = counts
            return  # return 해줘야 더이상 안움직일껄요

    for k in range(4):  # 모든 방향을 고려합시다.
        if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N:  # 일단 최초의 전제 조건은 범위 밖을 나가면 안됨
            if visited[ni + di[k]][nj + dj[k]] == 0 and ARR[ni + di[k]][nj + dj[k]] != 'T':  # 처음 가는 곳인데 나무가 없다면!
                if abs(d-k) == 3:  # 방향 차이가 3이라면! (이건 k, d가 0, 3일때를 고려한건데 사실상 1 차이나는건데 얘는 인식하지 못하니깐)
                    visited[ni + di[k]][nj + dj[k]] = 1  # visited 찍고
                    dfs(ni + di[k], nj + dj[k], k, cutting, counts + 2)  # 방향 1 돌렸고, 앞으로 한번 갔으니깐 조작은 2회
                    visited[ni + di[k]][nj + dj[k]] = 0  # 재귀함수에서 나왔으니 원본 맞춰줘야하니깐 visited 다시 없애주고
                else:  # 방향차이가 0, 1, 2라면!
                    visited[ni + di[k]][nj + dj[k]] = 1  # visited 찍고
                    dfs(ni + di[k], nj + dj[k], k, cutting, counts + abs(d-k) + 1)  # 방향돌린만큼(0, 1, 2)회 + 전진 1회
                    visited[ni + di[k]][nj + dj[k]] = 0  # 재귀함수에서 나왔으니 원본 맞춰줘야하니깐 visited 다시 없애주고
            elif cutting < K and visited[ni + di[k]][nj + dj[k]] == 0 and ARR[ni+di[k]][nj+dj[k]] == 'T':
                # 나무 자를 수 있는 횟수가 남아있어야하고, 한번도 방문안했고, 내 눈앞에는 나무가 있다면!
                ARR[ni + di[k]][nj + dj[k]] = 'G'  # 일단 나무를 베어서 땅으로 만들어
                # 위와 동일하고
                if abs(d-k) == 3:
                    visited[ni + di[k]][nj + dj[k]] = 1
                    dfs(ni + di[k], nj + dj[k], k, cutting + 1, counts + 2)
                    visited[ni + di[k]][nj + dj[k]] = 0
                else:
                    visited[ni + di[k]][nj + dj[k]] = 1
                    dfs(ni + di[k], nj + dj[k], k, cutting + 1, counts + abs(d-k) + 1)
                    visited[ni + di[k]][nj + dj[k]] = 0
                # 여기까지 위와 동일하고
                ARR[ni + di[k]][nj + dj[k]] = 'T'  # 재귀함수 다 빠져나왔으니 원본 맞춰야하니깐 다시 나무도 원상복귀


T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())
    ARR = [list(input()) for _ in range(N)]
    min_control = 4 * N**2 + 1
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if ARR[i][j] == 'X':
                si, sj = i, j

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    visited[si][sj] = 1

    dfs(si, sj, 0, 0, 0)

    if min_control == 4 * N**2 + 1:  # 다 돌렸는데 왜 횟수가 똑같지?
        min_control = -1  # 거긴 못가는 곳이었던거지 차윤이는 계속 울어 아빠는 갈게

    print(f'#{TEST_CASE} {min_control}')
