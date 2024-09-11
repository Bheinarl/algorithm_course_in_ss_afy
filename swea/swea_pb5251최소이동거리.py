import heapq

def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def dijk(idx):

    q = []

    for da in adjL
        heapq.heappush(da)

    while q:



T = int(input())
for TEST_CASE in range(1, T+1):
    N, E = map(int, input().split())
    rep = [t for t in range(N)]
    distance = [int(1e9)]*N
    for u in range(E):
        s, e, w = map(int, input().split())


    dijk(0)