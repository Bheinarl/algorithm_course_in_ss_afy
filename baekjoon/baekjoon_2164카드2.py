N = int(input())
arr = []

for l in range(1, N+1):
    arr += [l]

i = 0
for _ in range(N-1):
    i += 1
    arr += [arr[i]]
    i += 1

print(arr[i])
