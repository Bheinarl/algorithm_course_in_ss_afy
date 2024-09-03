def f(i):

    if i == n:
        pass
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            f(i+1)
            p[i], p[j] = p[j], p[i]


# 0 0 / 1 1 / 2 2 / 3 4

n = 5
p = [1, 2, 3, 4, 5]
f(0)
# 5개를 순열하고 싶다.