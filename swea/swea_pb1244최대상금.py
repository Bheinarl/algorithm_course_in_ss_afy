def f(counts):
    global max_price

    if counts == M or counts == N:

        price = ''
        for txt in ARR:
            price += txt
        max_price = max(max_price, int(price))
        return

    else:
        for i in range(N-1):
            for j in range(i+1, N):
                ARR[i], ARR[j] = ARR[j], ARR[i]
                f(counts + 1)
                ARR[i], ARR[j] = ARR[j], ARR[i]


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR, M = map(int, input().split())
    ARR = list(str(ARR))
    N = len(ARR)
    max_price = 0

    f(0)

    print(f'#{TEST_CASE} {max_price}')
