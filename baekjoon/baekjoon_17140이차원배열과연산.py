def R_operation(arr):
    new_arr = []
    max_len = 0

    for row in arr:
        count = {}

        # 개수 카운트
        for x in row:
            if x == 0:  # 0은 무시
                continue
            if x not in count:
                count[x] = 1
            elif x in count:
                count[x] += 1

        # [(숫자, 횟수)] 리스트 생성
        pairs = []
        for num in count:
            pairs.append((num, count[num]))

        # 정렬 (횟수, 숫자 순으로)
        pairs.sort(key=lambda x: (x[1], x[0]))

        # 배열로 변환
        new_row = []
        for num, cnt in pairs:
            new_row.append(num)
            new_row.append(cnt)

        # 길이 제한
        new_row = new_row[:100]
        max_len = max(max_len, len(new_row))
        new_arr.append(new_row)

    # 0 패딩
    for row in new_arr:
        while len(row) < max_len:
            row.append(0)

    return new_arr


def C_operation(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    new_cols = []
    max_len = 0

    # 각 열 처리 (R_operation과 동일한 방법)
    for c in range(col_len):
        count = {}

        for r in range(row_len):
            x = arr[r][c]
            if x == 0:
                continue
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        pairs = []
        for num in count:
            pairs.append((num, count[num]))

        pairs.sort(key=lambda x: (x[1], x[0]))

        new_col = []
        for num, cnt in pairs:
            new_col.append(num)
            new_col.append(cnt)

        new_col = new_col[:100]
        max_len = max(max_len, len(new_col))
        new_cols.append(new_col)

    # 열 패딩
    for col in new_cols:
        while len(col) < max_len:
            col.append(0)

    # 열 -> 행 재구성
    new_arr = []
    for r in range(max_len):
        row = []
        for c in range(len(new_cols)):
            row.append(new_cols[c][r])
        new_arr.append(row)

    return new_arr


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

time = 0

while time <= 100:
    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break

    if len(A) >= len(A[0]):
        A = R_operation(A)
    else:
        A = C_operation(A)

    time += 1
else:
    print(-1)