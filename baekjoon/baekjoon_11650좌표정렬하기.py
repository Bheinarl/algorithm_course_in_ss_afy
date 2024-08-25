N = int(input())
arr = []
for _ in range(N):
    arr += [list(map(int, input().split()))]

arr.sort(key=lambda x: (x[0], x[1]))

for arr_arr in arr:
    print(*arr_arr)
