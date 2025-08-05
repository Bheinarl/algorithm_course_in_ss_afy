C, N = map(int, input().split())
advertisements = [tuple(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * 10000  # C의 최댓값은 1000
dp[0] = 0  # 0명 확보에 드는 비용은 0원

for cost, customer in advertisements:
    for i in range(customer, 10000):
        dp[i] = min(dp[i], dp[i - customer] + cost)

# 최소 C명 이상 확보하는데에 필요한 최소 비용
print(min(dp[C:]))