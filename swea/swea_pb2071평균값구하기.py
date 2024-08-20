T = int(input())

for test_case in range(1, T+1):

    arr = list(map(int, input().split()))

    sum_num = 0

    for num in arr:
        if num % 2 == 1:
            sum_num += num

    result = sum_num

    print(f'#{test_case} {result}')
