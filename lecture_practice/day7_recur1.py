def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return 1
    else:
        n * f(n-1)


cnt = 0
f(1000)
print(cnt)