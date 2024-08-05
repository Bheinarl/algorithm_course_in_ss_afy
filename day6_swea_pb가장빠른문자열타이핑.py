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
