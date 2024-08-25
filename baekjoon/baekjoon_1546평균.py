N = int(input())
arr = list(map(int, input().split()))

M = max(arr)

for i in range(N):
    arr[i] = arr[i] / M * 100

sum_new = sum(arr)
print(sum_new/N)