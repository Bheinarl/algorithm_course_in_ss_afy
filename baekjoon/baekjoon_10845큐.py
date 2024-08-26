def f_push(x):
    ARR.append(x)
    return


def f_pop():
    if ARR:
        print(ARR.pop(0))
    else:
        print(-1)
    return


def f_size():
    print(len(ARR))
    return


def f_empty():
    if ARR:
        print(0)
    else:
        print(1)
    return


def f_front():
    if ARR:
        print(ARR[0])
    else:
        print(-1)
    return


def f_back():
    if ARR:
        print(ARR[-1])
    else:
        print(-1)
    return


N = int(input())
ARR = []

for _ in range(N):
    lst = list(input().split())

    if len(lst) != 1 and lst[0] == 'push':
        f_push(lst[1])
    elif lst[0] == 'pop':
        f_pop()
    elif lst[0] == 'size':
        f_size()
    elif lst[0] == 'empty':
        f_empty()
    elif lst[0] == 'front':
        f_front()
    elif lst[0] == 'back':
        f_back()
