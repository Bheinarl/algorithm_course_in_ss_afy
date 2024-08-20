from sys import stdin

W, H = map(int, stdin.readline().split())
p, q = map(int, stdin.readline().split())
T = int(stdin.readline())

a = (p+T) // W
b = (q+T) // H

if a % 2 == 0:
    p = (p+T) % W
else:
    p = W - (p+T) % W

if b % 2 == 0:
    q = (q+T) % H
else:
    q = H - (q+T) % H

print(f'{p} {q}')
