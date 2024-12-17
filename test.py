def change2bit(word):
    bit_mask = 0
    for char in word:
        bit_mask |= 1 << (ord(char) - ord('a'))  # |= : 해당 비트가 0이면 1로 변환
    return bit_mask


words = []
start_bit_mask = 0
for char in 'aabbb':
    start_bit_mask |= change2bit(char)
    print(start_bit_mask)

# print(start_bit_mask)