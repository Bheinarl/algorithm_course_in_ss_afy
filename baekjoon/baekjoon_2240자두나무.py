T, W = map(int, input().split())

plum_tree = [0]
for _ in range(T):
    plum_tree.append(int(input()))

jadu = [[[0] * 2 for _ in range(W + 1)] for _ in range(T + 1)]

for t in range(1, T + 1):
    for w in range(W + 1):

        plum_drop_position = plum_tree[t]

        if w == 0:  # 초기 설정 / 한 번도 안 움직임 (1번 나무에 계속 있어봐)
            jadu[t][w][0] = jadu[t - 1][w][0] + (1 if plum_drop_position == 1 else 0)
        else:
            # 1번 나무에 있을래
            jadu[t][w][0] = max(jadu[t - 1][w][0], jadu[t - 1][w - 1][1]) + (1 if plum_drop_position == 1 else 0)

            # 2번 나무에 있을래
            jadu[t][w][1] = max(jadu[t - 1][w - 1][0], jadu[t - 1][w][1]) + (1 if plum_drop_position == 2 else 0)

ans = 0
for w in range(W + 1):
    ans = max(ans, jadu[T][w][0], jadu[T][w][1])

print(ans)
