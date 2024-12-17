import sys

def count_readable_words(words, learned_bitmask):  # 읽을 수 있는 단어를 count
    counts = 0
    for word_bitmask in words:  # 단어(비트마스킹된) 중에서
        if word_bitmask & learned_bitmask == word_bitmask:  # 단어의 비트마스크가 배운 알파벳의 비트마스크에 모두 1이면
            counts += 1
    return counts


def teach(index, count, learned_bitmask):  # 백트래킹을 이용한 알파벳 학습
    global max_words_counts

    if count == K - 5:  # 배울 수 있는 횟수 채우면 (antic 5개 제외)
        readable_words = count_readable_words(words, learned_bitmask)  # 읽을 수 있는 단어 수
        max_words_counts = max(max_words_counts, readable_words)  # 최댓값
        return

    for i in range(index, 26):
        if not (learned_bitmask & (1 << i)):  # 아직 배우지 않은 알파벳이라면
            teach(i + 1, count + 1, learned_bitmask | (1 << i))  # i번째 알파벳을 배웠다고 표시


def change2bit(word):  # 단어를 비트마스킹
    bit_mask = 0
    for char in word:
        bit_mask |= 1 << (ord(char) - ord('a'))  # |= : 해당 비트가 0이면 1로 변환
    return bit_mask


N, K = map(int, sys.stdin.readline().split())
if K < 5:  # 5개는 필수로 배워야하므로 K가 5보다 작으면 끝
    print(0)
    exit()

words = []
start_bit_mask = 0
for char in 'antic':
    start_bit_mask |= change2bit(char)  # antic은 시작 비트마스크로 저장

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(change2bit(word))  # 단어를 비트마스킹하여 저장

max_words_counts = 0
teach(0, 0, start_bit_mask)

print(max_words_counts)