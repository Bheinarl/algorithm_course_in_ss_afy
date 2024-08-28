def f(idx):
    if 2 * i + 1 > N:  # 자식 노드가 1개일 때
        heap[idx] = heap[2 * idx]
    else:  # 자식 노드가 2개일 때
        heap[idx] = heap[2*idx] + heap[2*idx + 1]


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M, L = map(int, input().split())

    heap = [0] * (N + 1)

    for _ in range(M):
        idx, val = map(int, input().split())
        heap[idx] = val

    for i in range(N, 0, -1):
        if 2 * i <= N and heap[i] == 0:  # 자식 노드가 하나라도 있거나, 노드의 키 값이 아직 안정해진 경우
            f(i)

    print(f'#{TEST_CASE} {heap[L]}')
