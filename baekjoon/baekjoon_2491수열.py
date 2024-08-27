N = int(input())
arr = list(map(int, input().split()))

i = 1
max_counts = 1
while i <= N-1:
    counts_i = 1
    while i <= N-1 and arr[i] >= arr[i-1]:
        counts_i += 1
        i += 1
    if counts_i > max_counts:
        max_counts = counts_i
    if i > N-1:
        break
    i += 1

j = 1
while j <= N-1:
    counts_j = 1
    while j <= N-1 and arr[j] <= arr[j-1]:
        counts_j += 1
        j += 1
    if counts_j > max_counts:
        max_counts = counts_j
    if j > N-1:
        break
    j += 1

print(max_counts)
