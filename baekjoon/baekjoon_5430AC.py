T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    x_input = input()

    if n == 0:
        x = []
    else:
        x = list(map(int, x_input[1:-1].split(',')))

    left = 0
    right = n - 1
    now_point = 'left'
    isError = False

    for RD in p:
        if RD == 'R':
            if now_point == 'left':
                now_point = 'right'
            else:
                now_point = 'left'
        else:
            if left > right:
                isError = True
                break
            if now_point == 'left':
                left += 1
            else:
                right -= 1

    if isError:
        print('error')
    else:
        ans = x[left:right+1]
        if now_point == 'right':
            ans = ans[::-1]
        print('[' + ','.join(map(str, ans)) + ']')
