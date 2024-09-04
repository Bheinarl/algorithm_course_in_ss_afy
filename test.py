def bug():
    start = 0
    while start + k < n:
        loc = 0
        if start + k >= n-1:
            return n
        else:
            for i in range(start + 1, min(start+1 + k, n-1)):
                if arr[i] == 1:
                    loc = i
            if loc == 0:
                return start + k+1
            else:
                start = loc

    return start + k + 1


t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    arr = list(map(int, input().split()))

    print(f'#{tc} {bug()}')