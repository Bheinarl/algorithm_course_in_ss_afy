import heapq

# BFS 를 하기 위해서는 모든 간선의 가중치가 동일해야 한다는 전제 조건이 필요


def dijkstra(n):
    q = []
    heapq.heappush(q, (0, n))
    # (count, 숫자) 반대로 하니깐 heapQ의 기능을 제대로 사용 불가
    # count 가 적을수록 먼저쓰고 싶은거라서 count 가 앞에 있어야함
    count_lst[n] = 0

    while q:
        counts, num = heapq.heappop(q)
        if count_lst[num] < counts:  # 혹시 모르니 한 번은 걸러주자
            continue

        # 어차피 count 가 적은 순서대로 저장되서 교체하거나 할 필요가 없네
        if 0 <= num * 2 <= 100000 and count_lst[num * 2] == int(1e9):
            heapq.heappush(q, (counts, num * 2))
            count_lst[num*2] = counts

        if 0 <= num + 1 <= 100000 and count_lst[num + 1] == int(1e9):
            heapq.heappush(q, (counts+1, num + 1))
            count_lst[num + 1] = counts + 1

        if 0 <= num - 1 <= 100000 and count_lst[num - 1] == int(1e9):
            heapq.heappush(q, (counts+1, num - 1))
            count_lst[num - 1] = counts + 1

    return count_lst[K]


N, K = map(int, input().split())
count_lst = [int(1e9)] * 100001
ans = dijkstra(N)
print(ans)
