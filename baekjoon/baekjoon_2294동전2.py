n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [100000] * (k + 1) # k가 10000을 넘지 않으므로 10000보다만 크면 된다.
dp[0] = 0  # 0원을 만드는 동전 개수는 0개

for coin in coins:
    for i in range(coin, k + 1):  # coin부터 k까지 모든 금액 최소 갯수
        dp[i] = min(dp[i], dp[i - coin] + 1)  # i원을 만들때 현재 동전을 사용할 때와 안할 때 중 최솟값

if dp[k] != 100000:
    print(dp[k])
else:
    print(-1)