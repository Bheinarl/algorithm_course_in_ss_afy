def f(i, N, sum_arr):

    global min_sum

    if i == N:
        if min_sum > sum_arr:
            min_sum = sum_arr
            return
        elif min_sum <= sum_arr:
            return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, sum_arr + ARR[i][p[i]])
            p[i], p[j] = p[j], p[i]
        return


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]
    p = [a for a in range(N)]
    min_sum = 10000
    sum_arr = 0
    f(0, N, sum_arr)

    print(f'#{TEST_CASE} {min_sum}')

"""
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