T = int(input())
for tc in range(1, T+1):
    s = input()
    n = len(s)
    ans = 1
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            ans = 0
            break
    print(f'#{tc} {ans}')
