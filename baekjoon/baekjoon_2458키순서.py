import sys

N, M = map(int, sys.stdin.readline().split())

lst = [[] for _ in range(N + 1)]

print(lst)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)

counts = 0
for num in range(1, N + 1):
    check_set = set()

    for i in len(lst):
        if num in lst[i]:
            set.add(i)
            stack.append(i)
    stack = []
    stack.append(lst[i])

    # 앞 뒤로 확인할꺼야. for문 돌려서 앞에 있는거 확인하고, 뒤에 있는거는 꼬리 물기 식으로 lst[num]에 있으면 계속 추가하는 방식