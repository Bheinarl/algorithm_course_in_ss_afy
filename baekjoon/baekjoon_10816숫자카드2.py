N = int(input())
ARR_N = list(map(int, input().split()))
M = int(input())
ARR_M = list(map(int, input().split()))

ARR_N.sort()

lst = {}

for i in range(N):
    if ARR_N[i] not in lst:
        lst[ARR_N[i]] = 1
    else:
        lst[ARR_N[i]] += 1

for j in range(M):
    if ARR_M[j] not in lst:
        print(0, end=' ')
    else:
        print(lst[ARR_M[j]], end=' ')
print()

"""
s = 0
e = N

for i in range(M):
    counts = 0
    while s <= e:
        mid = (s + e) // 2
        if ARR_N[mid] == ARR_M[i]:
            counts += 1

        if ARR_N[mid] >
"""