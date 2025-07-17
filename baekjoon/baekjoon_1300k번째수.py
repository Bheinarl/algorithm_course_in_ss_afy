def counting(x):
    counts = 0
    for i in range(1, N + 1):
        counts += min(x // i, N)
    return counts

N = int(input())
K = int(input())

left, right = 1, K
answer = 0

while left <= right:
    mid = (left + right) // 2
    if counting(mid) >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)