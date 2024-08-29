T = int(input())
num_alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, T + 1):
    lst = list(input())
    arr = []
    for i in range(10):
        n = 6
        sum_n = 0
        for j in range(7):
            if lst[7*i+j] == '1':
                sum_n += 2**n
            n -= 1
        arr += [sum_n]

    print(f'#{tc} ', end='')
    print(*arr)
