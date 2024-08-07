def fibonacci1(n):  # Memoization 을 이용한 방법
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci1(n-1) + fibonacci1(n-2)
    return memo[n]


def fibonacci(n):  # 재귀 함수를 이용한 방법
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


N = 7
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
print(fibonacci1(N))
print(fibonacci(N))
