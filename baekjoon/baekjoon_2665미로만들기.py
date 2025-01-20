import heapq

N = int(input())
MAZE = [input().strip() for _ in range(N)]

change_color = [[2501] * N for _ in range(N)]  # 50 * 50이 최대니깐
change_color[0][0] = 0  # 시작점에서는 색을 한 번도 안바꿔요

HQ = [(0, 0, 0)]  # 우선순위 큐 (바꾼 횟수, i, j)

while HQ:
    counts, i, j = heapq.heappop(HQ)

    if (i, j) == (N-1, N-1):  # 끝 지점에 도달하면 종료
        print(counts)
        exit()

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < N:
            if MAZE[ni][nj] == '0':  # 검은 방이면
                new_counts = counts + 1  # 바꿔야겠지?
            else:  # 아니면
                new_counts = counts  # 안바꿔도 되지

            if new_counts < change_color[ni][nj]:  # 지금까지 바꾼 횟수가 적으면
                change_color[ni][nj] = new_counts  # 갱신해
                heapq.heappush(HQ, (new_counts, ni, nj))  # 그리고 우선순위 큐에 넣어

print(change_color[N-1][N-1])