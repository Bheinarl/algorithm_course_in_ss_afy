a, b = map(int, input().split())

if a > b:
    if a - b == 1:
        print('A')
    elif a - b == 2:
        print('B')
elif a < b:
    if b - a == 1:
        print('B')
    elif b - a == 2:
        print('A')
