n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만들 수 있는 방법 1가지

for coin in coins:  # 1, 2, 5원을 사용할 수 있으므로
    for i in range(coin, k + 1):  # i 원을 만들기 위해서 coin원 동전을 추가한다면
        dp[i] += dp[i - coin]  # i - coin을 만들 수 있는 방법을 더한다.

print(dp[k])