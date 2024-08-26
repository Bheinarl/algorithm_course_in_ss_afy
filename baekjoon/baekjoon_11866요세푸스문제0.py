N, K = map(int, input().split())

lst = [n for n in range(1, N+1)]
i = 0
arr = []
for q in range(N):
    i = (i+K-1) % len(lst)
    arr.append(lst.pop(i))

print('<', end='')
for j in range(N):
    if j != N-1:
        print(f'{arr[j]}, ', end='')
    if j == N-1:
        print(f'{arr[j]}', end='')
print('>')
