T = int(input())

for test_case in range(1, T+1):

    arr = list(map(int, input().split()))

    max_num = 0
    for i in range(len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]

    print(f'#{test_case} {max_num}')
