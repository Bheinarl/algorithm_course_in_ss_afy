def f(n, arr):
    # 전선은 2로 표시
    # 1. 테두리 말고 중앙 프로세서 찾기
    # 2. 한 방향으로만 연결할 수 있는 프로세서 검색
    # 3. 이 프로세서들 전선 연결
    # 4. i j 흐름에 따라서 상하좌우 스캔후 가장 짫은 곳으로 연결

    # 모든 프로세서 좌표 -> lst_processor
    lst_processor = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                lst_processor += [[i, j]]

    # 주변말고 배열 가운데에 있는 프로세서 찾기 -> lst_processor_middle
    lst_processor_middle = []
    for k in range(len(lst_processor)):
        if 0 not in lst_processor[k] and n-1 not in lst_processor[k]:
            lst_processor_middle += [lst_processor[k]]

    # 4 방향 다 막힌 프로세서 찾아서 제거
    lst_non_blocked_processor = []
    for processor in lst_processor_middle:
        counts = 0
        [x, y] = processor

        for i in range(0, x):
            if arr[i][y] == 1:
                counts += 1
                break

        for i in range(x + 1, n):
            if arr[i][y] == 1:
                counts += 1
                break

        for j in range(0, y):
            if arr[x][j] == 1:
                counts += 1
                break

        for j in range(y + 1, n):
            if arr[x][j] == 1:
                counts += 1
                break

        if counts < 4:
            lst_non_blocked_processor += [processor]



    # 한 방향만 뚫린 프로세서 찾기 -> lst_blocked_processor
    lst_blocked_processor = []
    for processor in lst_non_blocked_processor:
        counts = 0
        [x, y] = processor

        for i in range(0,x):
            if arr[i][y] == 1:
                counts += 1
                break

        for i in range(x+1, n):
            if arr[i][y] == 1:
                counts += 1
                break

        for j in range(0,y):
            if arr[x][j] == 1:
                counts += 1
                break

        for j in range(y+1, n):
            if arr[x][j] == 1:
                counts += 1
                break

        if counts == 3:
            lst_blocked_processor += [processor]

    # 한 방향만 뚫린 프로세서 전선 연결
    for blocked_processor in lst_blocked_processor:
        [x, y] = blocked_processor

        for i in range(0, x):
            if arr[i][y] != 0:
                break
        else:
            for i in range(0, x):
                arr[i][y] = 2

        for i in range(x+1, n):
            if arr[i][y] != 0:
                break
        else:
            for i in range(x+1, n):
                arr[i][y] = 2

        for j in range(0, y):
            if arr[x][j] != 0:
                break
        else:
            for j in range(0, y):
                arr[x][j] = 2

        for j in range(y+1, n):
            if arr[x][j] != 0:
                break
        else:
            for j in range(y+1, n):
                arr[x][j] = 2

    # 행렬 가운데에 있는 프로세서 중 위에서 연결한 프로세서 제외한 목록
    lst_processor_middle_nonblocked = []
    for i in lst_non_blocked_processor:
        if i not in lst_blocked_processor:
            lst_processor_middle_nonblocked += [i]

    # 이제 가운데 있고 위에서 처리 안된 애들만 최소 길이로 연결
    for i in lst_processor_middle_nonblocked:
        [x, y] = i
        lst_dir = []
        for p in range(0, x):
            if arr[p][y] != 0:
                lst_dir += [99]
                break
        else:
            lst_dir += [x]

        for p in range(x + 1, n):
            if arr[p][y] != 0:
                lst_dir += [99]
                break
        else:
            lst_dir += [n-x-1]

        for q in range(0, y):
            if arr[x][q] != 0:
                lst_dir += [99]
                break
        else:
            lst_dir += [y]

        for q in range(y + 1, n):
            if arr[x][q] != 0:
                lst_dir += [99]
                break
        else:
            lst_dir += [n-y-1]

        min_dir = min(lst_dir)
        if min_dir == lst_dir[0]:
            for a in range(x):
                arr[a][y] = 2
        elif min_dir == lst_dir[2]:
            for b in range(y):
                arr[x][b] = 2
        elif min_dir == lst_dir[1]:
            for a in range(x+1, n):
                arr[a][y] = 2
        elif min_dir == lst_dir[3]:
            for b in range(y+1, n):
                arr[x][b] = 2

    # 2의 갯수(전선의 갯수))를 세야해
    counts_2 = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                counts_2 += 1

    return counts_2


T = int(input())
for TEST_CASE in range(1, T + 1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f(N, ARR)

    print(f'#{TEST_CASE} {RESULT}')
