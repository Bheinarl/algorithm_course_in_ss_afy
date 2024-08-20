T = int(input())

for test_case in range(1, T+1):

    arr = list(map(int, input().split()))

    sum_num = 0

    for num in arr:
        sum_num += num

    result = int(round(sum_num / len(arr), 0))

    print(f'#{test_case} {result}')
