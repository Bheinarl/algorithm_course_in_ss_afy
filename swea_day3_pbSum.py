def max_matrix_sum(arr):

    max_sum = 0
    left2right_cross_sum = 0
    right2lest_cross_sum = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:
                left2right_cross_sum += arr[i][j]

            if 99 - i == j:
                right2lest_cross_sum += arr[i][j]

        if row_sum > max_sum:
            max_sum = row_sum

        if col_sum > max_sum:
            max_sum = col_sum

    if left2right_cross_sum > max_sum:
        max_sum = left2right_cross_sum

    if right2lest_cross_sum > max_sum:
        max_sum = right2lest_cross_sum

    result = max_sum

    return result

for _ in range(10):
    test_case = int(input())

    arr = []

    for _ in range(100):
        arr += [list(map(int,input().split()))]

    result = max_matrix_sum(arr)

    print(f'#{test_case} {result}')