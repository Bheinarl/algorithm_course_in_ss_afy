N = int(input())
arr = []
for _ in range(N):
    arr += [int(input())]
arr.sort()
for i in range(N):
    print(arr[i])
