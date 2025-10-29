import sys

char = sys.stdin.readline().rstrip()
n = len(char)

def kmp(start):

    m = n - start  # 이번에 볼 접미사 길이
    pi = [0] * m  # 접두사 함수(pi) 배열: 길이 m, 모두 0으로 초기화
    ans = 0  # 이 접미사에서 관측한 pi 값의 최댓값
    j = 0  # 현재까지 일치한 접두사 길이 & 다음 비교할 접두사 인덱스

    for i in range(1, m):
        while j > 0 and char[start + i] != char[start + j]:  # s[start + i] (현재 문자)와 s[start + j] (이어질 접두사 다음 문자)가 다르면
            j = pi[j - 1]  # j를 줄여서 가장 긴 이전 경계로

        if char[start + i] == char[start + j]:  # 같으면 다음 문자도 비교
            j += 1
            pi[i] = j

            if j > ans:
                ans = j

    return ans  # char[start:]에서 가능한 최대 길이

answer = 0

# 모든 시작점 st에 대해 s[st:] 접미사를 보며 최대 경계 길이를 계산
for st in range(n):
    cur = kmp(st)  # s[st:]에서의 최대 pi 값
    if cur > answer:
        answer = cur

print(answer)