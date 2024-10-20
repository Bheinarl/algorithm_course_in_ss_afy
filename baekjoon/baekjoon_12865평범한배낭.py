import sys


N, K = map(int, sys.stdin.readline().split())

package = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    package.append((W, V))

# DP 테이블 초기화
dp = [0] * (K + 1)

# DP
for W, V in package:
    # 무게가 큰 것부터 처리해야 이전 값에 영향을 주지 않음
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
"""
예제와 같이 package 가 
6 13
4 8
3 6
5 12
일때
1. 무게가 6이니깐, 이 짐은 dp[6]과 dp[7]에 들어갈 수 있다. dp[6]=13, dp[7]=13
2. 무게가 4이니깐, 이 짐은 4, 5, 6, 7에 들어갈 수 있는데, 비교하잖아. 그래서 dp[5]=8, dp[4]=8
3. 무게가 3이니깐, 이 짐은 3, 4, 5, 6, 7에 들어갈 수있다. 비교하면, dp[7]보다 dp[4]+V가 더 크므로 dp[7]=dp[4]+V=14
   나머지 다 안되고 dp[3]=6이 저장됨 
   
...

이런 식으로 진행이 됩니다.

1차원 배열을 최대한 써보는게 좋다고 했던거 같아요 py.june님이 
"""

print(dp[K])
