import sys
input = sys.stdin.readline

n = int(input())
diff = [0] * 368  # 아마 366까지 쓸텐데 여유롭게 처리함

for _ in range(n):
    start_day, end_day = map(int, input().split())
    diff[start_day] += 1
    diff[end_day + 1] -= 1  # +1 해준거 초기화

total = 0
cur = 0
width = 0
block_max = 0

for day in range(1, 367):
    cur += diff[day]
    if cur > 0:
        width += 1
        if cur > block_max:
            block_max = cur
    else:
        if width > 0:
            total += width * block_max
            width = 0
            block_max = 0

print(total)