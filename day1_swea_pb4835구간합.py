T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_num_min = 0
    sum_num_max = 0

    for i in range(0, N-M+1):

        sum_num = 0

        for j in range(i, i+M):
            sum_num += arr[j]

        if sum_num_min == 0 and sum_num_max == 0:
            sum_num_min = sum_num
            sum_num_max = sum_num
        else:
            if sum_num > sum_num_max:
                sum_num_max = sum_num

            if sum_num < sum_num_min:
                sum_num_min = sum_num

    result = sum_num_max - sum_num_min

    print(f'#{test_case} {result}')