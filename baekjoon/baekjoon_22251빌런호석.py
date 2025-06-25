N, K, P, X = map(int, input().split())

LED = [
    "1111110", "0110000", "1101101", "1111001", "0110011",
    "1011011", "1011111", "1110000", "1111111", "1111011"
]

def count_diff(a, b):
    counts = 0
    for i in range(7):
        if LED[a][i] != LED[b][i]:
            counts += 1
    return counts

def get_digits(n):
    s = str(n).zfill(K)
    return list(map(int, s))

answer = 0
for num in range(1, N + 1):
    if num == X:
        continue
    total_diff = 0
    cur_digits = get_digits(X)
    new_digits = get_digits(num)
    for d1, d2 in zip(cur_digits, new_digits):
        total_diff += count_diff(d1, d2)
        if total_diff > P:
            break
    if total_diff <= P:
        answer += 1

print(answer)
