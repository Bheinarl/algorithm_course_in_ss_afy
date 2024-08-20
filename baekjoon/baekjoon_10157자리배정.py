def f():  # 델타 썼는데 시간초과 뜸
    global N
    global M
    global K

    if K > N*M:
        return 0, 0
    else:
        x = 1
        y = 0
        z = 0

        while K > 0 and M >= 0 and N >= 0:
            if z == 0:
                if K >= N:
                    y += N
                    K -= N
                    M -= 1
                    z = 1
                else:
                    y += K
                    K = 0
            elif z == 1:
                if K >= M:
                    x += M
                    K -= M
                    N -= 1
                    z = 2
                else:
                    x += K
                    K = 0
            elif z == 2:
                if K >= N:
                    y -= N
                    K -= N
                    M -= 1
                    z = 3
                else:
                    y -= K
                    K = 0
            elif z == 3:
                if K >= M:
                    x -= M
                    K -= M
                    N -= 1
                    z = 0
                else:
                    x -= K
                    K = 0

    return x, y


M, N = map(int, input().split())
K = int(input())

x, y = f()
if x == 0:
    print(0)
else:
    print(f'{x} {y}')
