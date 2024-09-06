def f(now_height, i):

    global min_height

    if i == N and now_height < B:  # 다 결정했는데 높이 도달 못하면 X
        return
    elif i == N:
        if min_height > now_height:
            min_height = now_height
    else:
        f(now_height + ARR[i], i+1)  # 넣거나
        f(now_height, i+1)  # 안넣거나


T = int(input())
for TEST_CASE in range(1, T+1):
    N, B = map(int, input().split())
    ARR = list(map(int, input().split()))

    min_height = sum(ARR)+1
    f(0, 0)

    print(f'#{TEST_CASE} {min_height - B}')
