import sys

CHAR1 = sys.stdin.readline().rstrip()
CHAR2 = sys.stdin.readline().rstrip()

L1 = len(CHAR1)
L2 = len(CHAR2)

DP = [[[0, ''] for _ in range(L2 + 1)] for _ in range(L1 + 1)] # 배열에 길이를 뜻하는 숫자만 넣는 것이 아닌 문자열까지 기록

for i in range(1, L1 + 1):  # i는 CHAR1을 어디까지 사용할 지. DP 범위에 따라서 i는 1 ~ L1
    for j in range(1, L2 + 1):  # j는 CHAR2를 어디까지 사용할 지. DP 범위에 따라서 j는 1 ~ L2
        if CHAR1[i-1] == CHAR2[j-1]:  # 둘의 글자가 같으면
            DP[i][j][0] = DP[i-1][j-1][0] + 1  # 지금까지 했던 수열(DP[i-1][j-1])에서 수열 길이 1 증가
            DP[i][j][1] = DP[i-1][j-1][1] + CHAR1[i-1]  # 글자 추가
        else:
            DP[i][j][0] = max(DP[i-1][j][0], DP[i][j-1][0])  # 둘의 글자가 다르면 상, 좌단 확인하여 최대값 기록
            if DP[i][j][0] == DP[i-1][j][0]:
                DP[i][j][1] = DP[i-1][j][1]  # 글자 그대로
            else:
                DP[i][j][1] = DP[i][j-1][1]  # 글자 그대로

print(DP[i][j][0])
print(DP[i][j][1])