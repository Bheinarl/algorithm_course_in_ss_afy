T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(0, N):
        max_height = 0
        if i == 0:
            max_height = arr[i+1]
            for j in range(0, 3):
                if i == j:
                    pass
                elif arr[j] > max_height:
                    max_height = arr[j]

            if max_height < arr[i]:
                result += arr[i] - max_height
        elif i == 1:
            max_height = arr[i-1]
            for j in range(0, 4):
                if i == j:
                    pass
                elif arr[j] > max_height:
                    max_height = arr[j]

            if max_height < arr[i]:
                result += arr[i] - max_height
        elif i == N-2:
            max_height = arr[i-2]
            for j in range(N-2, 10):
                if i == j:
                    pass
                elif arr[j] > max_height:
                    max_height = arr[j]

            if max_height < arr[i]:
                result += arr[i] - max_height
        elif i == N-1:
            max_height = arr[i-2]
            for j in range(N-3, 10):
                if i == j:
                    pass
                elif arr[j] > max_height:
                    max_height = arr[j]

            if max_height < arr[i]:
                result += arr[i] - max_height
        else:
            max_height = arr[i-2]
            for j in range(i-2, i+3):
                if i == j:
                    pass
                elif arr[j] > max_height:
                    max_height = arr[j]

            if max_height < arr[i]:
                result += arr[i] - max_height

    print(f'#{test_case} {result}')