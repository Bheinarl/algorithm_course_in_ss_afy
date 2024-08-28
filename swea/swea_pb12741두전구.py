T = int(input())
arr = []
for i in range(1, T + 1):
    AS, AE, BS, BE = map(int, input().split())

    arr += [max(0, min(AE, BE) - max(AS, BS))]

for i in range(T):
    print(f'#{i + 1} {arr[i]}')
