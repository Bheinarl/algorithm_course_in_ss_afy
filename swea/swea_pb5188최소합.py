def f(i, j, sum_num):  # i, j는 index, sum_num 은 이동하면서의 합계
    global min_sum

    if i >= N or j >= N:  # 인덱스가 초과하면 X
        return
    elif sum_num >= min_sum:  # 최소합보다 크면 X
        return
    elif i == N-1 and j == N-1:  # i, j가 왼쪽 끝에 해당하면
        sum_num += ARR[i][j]  # 이동하면서 이동하기 전 위치의 숫자를 더하므로 도착점에 도달하면 계산해줘야 함
        if min_sum > sum_num:
            min_sum = sum_num
    else:
        f(i+1, j, sum_num + ARR[i][j])  # 아래쪽으로 이동
        f(i, j+1, sum_num + ARR[i][j])  # 오른쪽으로 이동


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]
    min_sum = 2 * 10 * N

    f(0, 0, 0)

    print(f'#{TEST_CASE} {min_sum}')
