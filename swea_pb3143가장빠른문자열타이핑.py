def find_len(string):  # len 함수
    length = 0
    for _ in string:
        length += 1
    return length


T = int(input())
for test_case in range(1, T+1):
    txt, pattern = map(str, input().split())

    len_p = find_len(pattern)  # 고지식한 패턴 검색 이용
    len_t = find_len(txt)
    i = 0
    j = 0

    counts = 0
    while i < len_t and j < len_p:
        if txt[i] == pattern[j]:  # 같으면 끝까지 같은지 확인
            i += 1
            j += 1
        else:  # 같지 않으면 전 순회에서 시작한 txt 의 다음 문자부터 순회
            i = i - j + 1
            j = 0

        if j == len_p:  # 끝까지 같은 문자가 있었다면 counts +1 / 문자열은 다음 인덱스부터 계속 검색
            counts += 1
            j = 0

    result = len_t - (len_p - 1) * counts

    print(f'#{test_case} {result}')

"""
def find_length(words):  # len 내장함수 대체
    counts = 0
    for _ in words:
        counts += 1
    return counts


def find_typing_number(a, b):
    len_a = find_length(a)
    len_b = find_length(b)

    counts_b = 0

    while b in a:  # b가 a에 없을 때까지 반복
        for idx in range(len_a):
            if b == a[idx:idx+len_b]:  # a에 b가 있으면 counts_b +1
                counts_b += 1
                a = a[0:idx] + a[idx+len_b:]  # a에 있는 첫 b 제거
    # index 순서가 망가져서 for 구문에서는 빠지는 b가 있으나, while 문을 거쳐 계속 검사하므로 언젠간 빠진다.
    # count 내장함수 쓰면 a에서 b를 없애지 않아도 되므로 문제 X
    result = len_a - (len_b - 1) * counts_b

    return result


T = int(input())
for test_case in range(1, T+1):
    A, B = map(str, input().split())

    RESULT = find_typing_number(A, B)

    print(f'#{test_case} {RESULT}')

"""

"""
counts_b = a.count(b)
result = len(a) - (len(b) - 1) * counts_b
"""
