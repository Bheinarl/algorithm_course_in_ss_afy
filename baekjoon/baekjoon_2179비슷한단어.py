import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

best_len = -1
best_i, best_j = 0, 1

# 접두사 길이 L을 1부터 최대 길이까지 늘려가며 하나씩 검사
for L in range(1, max_len + 1):
    dict_prefix = {}  # { 접두사 : (가장 작은 인덱스, 두 번째로 작은 인덱스) }

    for idx, word in enumerate(words):
        if len(word) < L:
            continue  # 단어 길이가 L보다 짧으면 패스

        prefix = word[:L]

        if prefix not in dict_prefix:
            # 첫 번째 접두사 단어
            dict_prefix[prefix] = (idx, -1)
        else:
            a, b = dict_prefix[prefix]
            if b == -1:
                # 두 번째 접두사 단어를 처음 추가하는 경우
                if idx == a:
                    continue
                # (a, idx) 중 작은 인덱스가 앞으로 오게 정렬
                if idx < a:
                    a, b = idx, a
                else:
                    b = idx
            else:
                # 이미 a, b 두 개가 있고, idx까지 세 개 중
                # 가장 작은 두 개만 남기기
                candidates = [a, b, idx]
                candidates.sort()
                a, b = candidates[0], candidates[1]
            dict_prefix[prefix] = (a, b)

    # 이 길이 L에서 생긴 접두사 그룹들을 확인
    for a, b in dict_prefix.values():
        if b == -1:
            continue  # 단어가 1개뿐인 접두사는 패스

        if a > b:
            a, b = b, a  # 단순 정렬

        if L > best_len:
            best_len = L
            best_i, best_j = a, b
        elif L == best_len:
            # 같은 길이면 입력 순서가 더 앞선 접두사 쌍을 선택
            if a < best_i or (a == best_i and b < best_j):
                best_i, best_j = a, b

print(words[best_i])
print(words[best_j])