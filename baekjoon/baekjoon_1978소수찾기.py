N = int(input())
arr = list(map(int, input().split()))

sosu = 0
for i in range(N):
    counts = 0
    for j in range(1, arr[i]+1):
        if arr[i] % j == 0:
            counts += 1

    if counts == 2:
        sosu += 1

print(sosu)