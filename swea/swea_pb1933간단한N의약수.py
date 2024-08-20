n = int(input())
i = 1
while i <= n:
    if n // i == n / i:
        print(i, end=' ')
    i += 1
