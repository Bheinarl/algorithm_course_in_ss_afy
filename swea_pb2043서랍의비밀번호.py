p, k = map(int, input().split())

counts = 1
while p != k:
    counts += 1
    k += 1
print(counts)