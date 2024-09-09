def f(i, lst):

    if i > N+1:
        return
    elif lst in temp:
        return
    elif len(lst) == M:
        temp.append(lst)
        print(*lst)
        return
    elif i == N+1 and len(lst) < M:
        return
    else:
        for j in range(1, N+1):
            if j >= i-1:
                f(i + 1, lst + [j])
                f(i + 1, lst)


N, M = map(int, input().split())
temp = []
f(1, [])