N = int(input())
arr = []
for _ in range(N):
    arr += [input()]
arr = list(set(arr))


max_word = 0
for z in range(len(arr)):
    if len(arr[z]) > max_word:
        max_word = len(arr[z])

lst = [[] for _ in range(max_word+1)]

for p in range(len(arr)):
    for q in range(1, max_word+1):
        if len(arr[p]) == q:
            lst[q] += [arr[p]]
            break

for k in range(max_word+1):
    lst[k].sort()

i = 1
while lst != [[] for _ in range(max_word+1)]:
    if len(lst[i]) != 0:
        print(lst[i].pop(0))
    else:
        i += 1
