def snail_sort(n):
    arr = [[0] * n for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    num = 2
    arr[0][0] = 1  # 첫 숫자는 찍어준다.

    while num <= n ** 2:  # 'num' 이 2부터 n^2 까지
        ni = 0
        nj = 0
        for _ in range(n ** 2 - 1):  # 1은 이미 찍었으므로 n^2-1 번 반복

            ni += di[k]  # 이동한다.
            nj += dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= n:  # 행렬의 상하좌우를 초과하는 곳으로 이동했다면,
                ni -= di[k]  # 다시 원상복구
                nj -= dj[k]
                k = (k + 1) % 4  # 델타 이용한 방향 전환
                ni += di[k]  # 다시 이동
                nj += dj[k]

            if arr[ni][nj] != 0:  # 찍고자하는 자리가 0이 아니라면
                ni -= di[k]  # 다시 원상복구
                nj -= dj[k]
                k = (k + 1) % 4  # 델타를 이용한 방향 전환
                ni += di[k]  # 다시 이동
                nj += dj[k]

            arr[ni][nj] = num  # 숫자 찍어준다
            num += 1

    return arr


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    result = snail_sort(N)

    print(f'#{test_case}')
    for a in result:
        print(*a)
