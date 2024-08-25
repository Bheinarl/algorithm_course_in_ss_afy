def f1(n):
    for k in range(len(n)//2):
        if n[len(n)//2 - 1 - k] != n[len(n)//2 + k]:
            return 'no'
    else:
        return 'yes'


def f2(n):
    for k in range(len(n)//2 + 1):
        if n[len(n)//2 - k] != n[len(n)//2 + k]:
            return 'no'
    else:
        return 'yes'


while True:
    N = input()

    if N == '0':
        break

    if len(N) % 2 == 0:
        print(f1(N))
        continue

    elif len(N) % 2 == 1:
        print(f2(N))
        continue
