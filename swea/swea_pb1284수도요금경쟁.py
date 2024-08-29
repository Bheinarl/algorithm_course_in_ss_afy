T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    a = P*W
    if W > R:
        b = Q+S*(W-R)
    else:
        b = Q

    print(f'#{tc} {min(a, b)}')