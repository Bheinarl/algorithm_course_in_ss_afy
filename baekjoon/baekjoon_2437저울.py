"""
import sys
input = sys.stdin.readline

N = int(input().strip())
weights = list(map(int, input().split()))
total = sum(weights)

dp = [False] * (total + 1)
dp[0] = True

for w in weights:
    # 뒤에서부터 순회해야 중복 사용 방지
    for i in range(total, -1, -1):
        if dp[i] and i + w <= total:
            dp[i + w] = True

# 못 만드는 가장 작은 무게 찾기
for i in range(1, total + 2):
    if i > total or not dp[i]:
        print(i)
        break
"""

import sys
input = sys.stdin.readline

N = int(input().strip())
weights = list(map(int, input().split()))
weights.sort()

able = 0
for w in weights:
    if w > able + 1:
        print(able + 1)
        break
    able += w
else:
    print(able + 1)