def find_len(string):  # len 함수
    counts = 0
    for _ in string:
        counts += 1
    return counts


T = int(input())
for test_case in range(1, T+1):  # 고지식한 패턴 검색 이용
    pattern = input()
    txt = input()

    len_p = find_len(pattern)
    len_t = find_len(txt)
    i = 0
    j = 0

    result = 0
    while i < len_t and j < len_p:
        if txt[i] == pattern[j]:  # 같으면 끝까지 같은지 확인
            i += 1
            j += 1
        else:  # 같지 않으면 전 순회에서 시작한 txt 의 다음 문자부터 순회
            i = i - j + 1
            j = 0

    if j == len_p:  # 끝까지 같은 문자가 있었다면 1 반환, 없었다면 0 반환
        result = 1

    print(f'#{test_case} {result}')
