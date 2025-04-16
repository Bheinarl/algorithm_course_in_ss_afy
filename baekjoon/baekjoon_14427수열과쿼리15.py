N = int(input())
A = list(map(int, input().split()))
M = int(input())

queries = []
for _ in range(M):
     Q = input().split()
     queries.extend(Q)

size = 1
while size < N:
    size *= 2
tree = [(float('inf'), -1)] * (2 * size)

for i in range(N):
    tree[size + i] = (A[i], i)

for i in range(size - 1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

def query1(index, value):  # 쿼리 1일 경우 값 바꿔주고 최소값 최신화
    idx = size + index
    tree[idx] = (value, index)
    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])

def query2():  # 쿼리 2일 경우 최소값 인덱스
    return tree[1][1] + 1  # 문제는 1-based index

output = []
idx = 0
for _ in range(M):
    t = int(queries[idx])
    if t == 1:
        i = int(queries[idx + 1]) - 1
        v = int(queries[idx + 2])
        query1(i, v)
        idx += 3
    else:
        output.append(str(query2()))
        idx += 1

print('\n'.join(output))


