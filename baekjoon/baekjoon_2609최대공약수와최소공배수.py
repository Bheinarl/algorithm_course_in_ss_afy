A, B = map(int, input().split())

A, B = min(A, B), max(A, B)

max_i = 0
for i in range(1, A+1):
    if A % i == 0 and B % i == 0 and max_i < i:
        max_i = i

print(max_i)
print(max_i * (A // max_i) * (B // max_i))
