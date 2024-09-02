def f(i):  # 순열로 줄부터 세우고 나서 계산
    global min_sum
    global lst

    if i == N-1:
        sum_num = 0
        arr = [0] + lst + [0]  #  처음과 끝은 고정하고 중간만 계산
        for k in range(N):
            sum_num += ARR[arr[k]][arr[k+1]]

        if min_sum > sum_num:
            min_sum = sum_num

    else:  # 사무실에서 출발해서 사무실로 도착하니깐 중간 순서만 순열하는 과정
        for j in range(i, N-1):
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    min_sum = 100 * N  # 최소값은 N 번만큼 가는데 다 100일 때
    lst = [o for o in range(1, N)]  # 중간 순서만 순열로 줄 세우려고 만든 list
    f(0)

    print(f'#{TEST_CASE} {min_sum}')
