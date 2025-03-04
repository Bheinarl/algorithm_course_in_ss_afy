n = int(input())
elec_lines = [list(map(int, input().split())) for _ in range(n)]

elec_lines.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if elec_lines[j][1] < elec_lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))