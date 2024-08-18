def f(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = f(n-1) + f(n-2)
    return memo[n]

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1

    ans = f(n)
    print(ans)

# k 1 2 3 4 6
# n 0 1 2 3 4 5 6 7

# 0   1             [1]
# 1   1 1           [1] [1]
# 2   1 2 1         [1] f(i-1)+f(i) [1]
# 3   1 3 3 1       [1] f(i-1)+f(i) f(i-1)+f(i) [1]
# 4   1 4 6 4 1
# 5   1 5 10 10 5 1       1, 1*5, 2*5, 2*5, 1*5 1
# 6   1 6 15 20 15 6 1    1, 6, 3*(6-1),
# 7   1 7 21 35 35 21 7 1   1, 1*7, 3*7, 5*7, 5*7, 3*7, 1*7, 1
# n   1 n n(n-1)/2
"""
for t in range(1, T + 1):  # 인덱스를 이용한 풀이

    n = int(input())
    arr = []
    for i in range(n):
        arr += [[0] * (i + 1)]  # 각 행에 숫자 넣을 크기만큼 [0]을 생성
        for j in range(i + 1):
            if j == 0:
                arr[i][j] = 1  # 각 행의 첫 번째 숫자는 무조건 1
            elif i == j:
                arr[i][j] = 1  # 각 행의 마지막 숫자는 무조건 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]  # 각 행의 중간은 위의 왼쪽 오른쪽 값의 합

    print(f'#{t}')
    for arr_arr in arr:
        print(*arr_arr)
"""
