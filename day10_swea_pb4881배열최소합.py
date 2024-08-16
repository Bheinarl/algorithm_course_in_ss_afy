def f1(ARR, idx, N):
    global min_sum
    if idx == N:
        one_each_col_sum = 0
        for k in range(N):
            one_each_col_sum += ARR[k][col_index[k]]
        if one_each_col_sum < min_sum:
            min_sum = one_each_col_sum
        return
    else:
        for j in range(idx, N):  # 순열에서 idx 는 자릿수, j는 idx 보다는 큰 idx 와 바꿀 수
            col_index[idx], col_index[j] = col_index[j], col_index[idx]
            f1(ARR, idx+1, N)
            col_index[idx], col_index[j] = col_index[j], col_index[idx]
        return


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    col_index = [q for q in range(N)]
    min_sum = 1000

    f1(ARR, 0, N)

    print(f'#{TEST_CASE} {min_sum}')

"""
1 2 3
4 5 6
7 8 9

123
123
123

123
132



"""