import sys
input = sys.stdin.readline

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = {char: i for i, char in enumerate(digits)}

N = int(input().strip())
number_36_digit = [input().strip() for _ in range(N)]
K = int(input().strip())

weight_sum_4_char = [0] * 36

total = 0

for s in number_36_digit:
    w = 1
    for char in reversed(s):
        v = value[char]
        total += v * w
        weight_sum_4_char[v] += w
        w *= 36

gain = [(35 - v) * weight_sum_4_char[v] for v in range(36)]
gain.sort(reverse=True)

for i in range(K):
    if gain[i] == 0:
        break
    total += gain[i]

if total == 0:
    print('0')
else:
    out = []
    t = total
    while t > 0:
        r = t % 36
        t = t // 36
        out.append(digits[r])
    print(''.join(reversed(out)))