# Memoization 을 이용한 방법
def f1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = f1(n-1) + 2 * f1(n-2)
    return memo[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    memo = [0] * (N+1)
    memo[0] = 1
    memo[1] = 1
    RESULT = f1(N)
    print(f'#{tc} {RESULT}')
"""
# 재귀 함수를 이용한 방법
def f2(n):
    if n < 2:
        return 1
    else:
        return f2(n-1) + 2 * f2(n-2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10
    memo = [0] * (N + 1)
    memo[0] = 1
    memo[1] = 1
    RESULT = f2(N)
    print(f'#{tc} {RESULT}')
"""
"""
# Index 를 이용한 풀이
T = int(input()) 
for tc in range(1, T+1):
    N = int(input())//10
    arr = []

    for _ in range(N+1):
        arr += [0]
    arr[0] = 1  # 초기값 설정
    arr[1] = 1  # 초기값 설정

    for i in range(2, N+1):  # i(index)는 2부터 N까지
        arr[i] = arr[i-1] + 2 * arr[i-2]  # 문제의 규칙

    ans = arr[N]
    print(f'#{tc} {ans}')
"""