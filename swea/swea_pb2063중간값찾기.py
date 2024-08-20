N = int(input())
arr = list(map(int, input().split()))

arr.sort()

mid_num = arr[(N+1)//2 - 1]

print(mid_num)
