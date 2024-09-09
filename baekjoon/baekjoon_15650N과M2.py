def f(i, lst):

    if i > N+1:
        return
    elif len(lst) == M:
        # for k in range(len(lst)):
        print(*lst)
    elif i == N+1 and len(lst) < M:
        return
    else:
        f(i + 1, lst + [i])
        f(i + 1, lst)


N, M = map(int, input().split())

lst = [n for n in range(1, N+1)]

f(1, [])