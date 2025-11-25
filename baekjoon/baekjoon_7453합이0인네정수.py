import sys
input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A+B 모든 합
AB_sums = [0] * (n * n)
idx = 0
for i in range(n):
    ai = A[i]
    for j in range(n):
        AB_sums[idx] = ai + B[j]
        idx += 1

# C+D 모든 합
CD_sums = [0] * (n * n)
idx = 0
for i in range(n):
    ci = C[i]
    for j in range(n):
        CD_sums[idx] = ci + D[j]
        idx += 1

AB_sums.sort()
CD_sums.sort()

len_ab = len(AB_sums)
len_cd = len(CD_sums)

i = 0
j = len_cd - 1
answer = 0

while i < len_ab and j >= 0:
    s = AB_sums[i] + CD_sums[j]

    if s == 0:
        # AB_sums[i] 와 같은 값 몇 개?
        av = AB_sums[i]
        cnt_a = 0
        while i < len_ab and AB_sums[i] == av:
            cnt_a += 1
            i += 1

        # CD_sums[j] 와 같은 값 몇 개?
        bv = CD_sums[j]
        cnt_b = 0
        while j >= 0 and CD_sums[j] == bv:
            cnt_b += 1
            j -= 1

        answer += cnt_a * cnt_b

    elif s < 0:
        i += 1
    else:
        j -= 1

print(answer)