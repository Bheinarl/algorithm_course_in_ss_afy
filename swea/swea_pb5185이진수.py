T = int(input())
num_alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, T + 1):
    N, lst = input().split()
    lst = list(lst)
    N = int(N)

    i = 0
    n = 0
    arr = []
    while i < N:
        if lst[i] in '0123456789':
            num = int(lst[i])
        else:
            num = num_alpha[lst[i]]

        i += 1
        n += 1

        for j in range(3, -1, -1):
            if num&(1<<j):
                arr += [1]
            else:
                arr += [0]

    print(f'#{tc} ', end='')
    for k in range(len(arr)):
        print(arr[k], end='')
    print()


"""
T = int(input())
num_alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, T + 1):
    N, lst = input().split()
    lst = list(lst)
    N = int(N)

    i = N - 1
    n = 0
    arr = []
    while i >= 0:
        if lst[i] in '0123456789':
            num = int(lst[i])
        else:
            num = num_alpha[lst[i]]

        for _ in range(4):
            arr += [num % 2]
            num //= 2

        i -= 1
        n += 1

    ans_arr = []
    for _ in range(len(arr)):
        ans_arr.append(arr.pop())

    print(f'#{tc} ', end='')
    for k in range(len(ans_arr)):
        print(ans_arr[k], end='')
    print()
"""