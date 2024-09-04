def f(level, sum_num):

    if level == 3 and sum_num not in path:
        path.append(sum_num)
        # print(sum_num)
        return
    elif level == 3 and sum_num in path:
        return
    else:

        for i in range(1, 7):
            f(level + 1, sum_num + i)


path = []
f(0, 0)
print(path)