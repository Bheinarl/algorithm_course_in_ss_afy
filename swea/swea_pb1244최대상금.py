def f(i, lst, counts):
    global max_price




T = int(input())
for TEST_CASE in range(1, T+1):
    ARR, M = map(int, input().split())
    ARR = list(str(ARR))
    N = len(ARR)
    max_price = 0
    f(0, [], 0)

    print(f'#{TEST_CASE} {max_price}')