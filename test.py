ARR = []
for _ in range(20):
    ARR += list(map(list, input().split()))

A = []
for i in range(13):
    A += ARR[i][0]
print(A)