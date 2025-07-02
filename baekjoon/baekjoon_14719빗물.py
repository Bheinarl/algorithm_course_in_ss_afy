H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0

for i in range(1, W - 1):  # 양 끝은 물이 고일 수 없음
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    min_height = min(left_max, right_max)

    if blocks[i] < min_height:
        result += min_height - blocks[i]

print(result)