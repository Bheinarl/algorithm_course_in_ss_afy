def f(idx, lst):
    global max_len

    if idx == N:
        if len(lst) > max_len:
            max_len = len(lst)

    for j in range(idx, N):
        if ARR[j] > lst[-1]:
            f(idx + 1, lst+[ARR[j]])
            f(idx + 1, lst)


N = int(input())
ARR = list(map(int, input().split()))

max_len = 0
for i in range(N):

    f(i, [ARR[i]])


print(max_len)
