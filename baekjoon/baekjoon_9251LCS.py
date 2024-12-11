import sys

CHAR1 = sys.stdin.readline().rstrip()
CHAR2 = sys.stdin.readline().rstrip()

L1 = len(CHAR1)
L2 = len(CHAR2)

"""
CHAR1를 순회해서 CHAR2에 같은 글자가 있으면 카운트를 늘려가는 식으로
근데 없을 수도 있으니깐 빈 칸부터 시작해야해.

  _ C A P C A K
_ 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1
C 0 1 1 1 2 2 2
A 0 1 2 2 2 3 3
Y 0 1 2 2 2 3 3
K 0 1 2 2 2 3 4
P 0 1 2 3 3 3 4

  _ A C A C A C
_ 0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
C 0 1 2 2 3 3 3
A 0 1 2 3 3 4 4
C 0 1 2 3 4 4 5
A 0 1 2 3 4 5 5

"""

DP = [[0] * (L2 + 1) for _ in range(L1 + 1)]

for i in range(1, L1 + 1):  # i는 CHAR1을 어디까지 사용할 지. DP 범위에 따라서 i는 1 ~ L1
    for j in range(1, L2 + 1):  # j는 CHAR2를 어디까지 사용할 지. DP 범위에 따라서 j는 1 ~ L2
        if CHAR1[i-1] == CHAR2[j-1]:  # 둘의 글자가 같으면
            DP[i][j] = DP[i-1][j-1] + 1  # 지금까지 했던 수열(DP[i-1][j-1])에서 수열 길이 1 증가
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])  # 둘의 글자가 다르면 상, 좌단 확인하여 최대값 기록

print(DP[i][j])