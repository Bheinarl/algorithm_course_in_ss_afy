from sys import stdin

t = int(input())
whole_arr = [[0 for _ in range(1001)] for _ in range(1001)]

for p in range(1, t + 1):
    x, y, n, m = map(int, stdin.readline().split())
    for i in range(x, x + n):
        for j in range(y, y + m):
            whole_arr[i][j] = p

arr_arr = [ 0 for _ in range(t)]
for a in range(1001):
    for b in range(1001):
        if whole_arr[a][b] != 0:
            arr_arr[whole_arr[a][b] - 1] += 1

for numb in arr_arr:
    print(numb)