N, M = map(int, input().split())
arr = list(map(int, input().split()))

nearM = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = arr[i] + arr[j] + arr[k]
            if nearM < sum_num <= M:
                nearM = sum_num

print(nearM)
