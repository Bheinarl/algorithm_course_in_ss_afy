T = int(input())
for TC in range(1, T+1):
    arr = list(map(input().split()))

    N = len(arr)
    stack = []

    for _ in range(N):
        