N = int(input())
A = list(map(int, input().split()))

increase = [1 for _ in range(N)]  # 올라가는 거
decrease = [1 for _ in range(N)]  # 내려가는 거

# 정방향으로 가면서
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j] + 1)  # 전 값보다 크면 계속 count

# 역방향으로 가면서
for p in range(N-1, -1, -1):
    for q in range(N-1, p, -1):
        if A[p] > A[q]:  # 전 값보다 크면 계속 count
            decrease[p] = max(decrease[p], decrease[q] + 1)  # 역방향이므로 전 값보다 크다는건 사실 작다는 것

ans = 0
for x in range(N):
    if ans < increase[x] + decrease[x] - 1:
        ans = increase[x] + decrease[x] - 1

print(ans)