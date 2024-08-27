def f(direc, loc):  # 일직선으로 생각

    if direc == 1:
        idx = loc
    elif direc == 4:
        idx = width + loc
    elif direc == 2:
        idx = width + height + width - loc
    else:
        idx = width + height + width + height - loc

    return idx


width, height = map(int, input().split())
N = int(input())
ARR = []
for _ in range(N):
    ARR += [list(map(int, input().split()))]

me_dir, me_loc = map(int, input().split())

sum_ans = 0
me_idx = f(me_dir, me_loc)

for i in range(N):
    direc = ARR[i][0]
    loc = ARR[i][1]
    idx = f(direc, loc)
    sum_ans += min(abs(me_idx - idx), abs(2*height + 2*width - abs(me_idx - idx)))

print(sum_ans)
