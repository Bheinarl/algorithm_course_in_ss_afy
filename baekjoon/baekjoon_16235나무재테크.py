N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]  # 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    # 봄
    dead_trees = [[0] * N for _ in range(N)]  # 죽은 나무들의 양분 저장
    for i in range(N):
        for j in range(N):
            if trees[i][j]:  # 나무가 존재할 때
                trees[i][j].sort()  # 나이 기준 오름차순으로 정렬
                new_trees = []  # 안죽은 나무
                for age in trees[i][j]:
                    if ground[i][j] >= age:  # 양분이 충분하면 성장
                        ground[i][j] -= age
                        new_trees.append(age + 1)
                    else:  # 양분이 부족하면 죽음
                        dead_trees[i][j] += age // 2  # 죽은 나무 양분이 됨
                trees[i][j] = new_trees  # 생존 나무 기록

    # 여름
    for i in range(N):
        for j in range(N):
            ground[i][j] += dead_trees[i][j]  # 여름에 죽은 나무 양분 추가

    # 가을
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:  # 5의 배수라면 번식
                    for d in range(8):
                        ni, nj = i + dx[d], j + dy[d]
                        if 0 <= ni < N and 0 <= nj < N:  # 범위 밖을 벗어나지 않으면
                            trees[ni][nj].append(1)  # 아기 나무 추가

    # 겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]  # 겨울마다 로봇이 양분 추가

result = sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(result)