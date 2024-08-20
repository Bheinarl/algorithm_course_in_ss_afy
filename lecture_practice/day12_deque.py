from collections import deque

deque_q = deque()
for i in range(1000000):
    deque_q.append(i)

for _ in range(1000000):
    deque_q.popleft()
print('end')


# 속도 차이가 많이 남
list_q = []
for i in range(1000000):
    list_q.append(i)

for _ in range(1000000):
    list_q.pop(0)
print('end')
