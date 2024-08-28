'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''


# 최대힙
def enq(n):  # 삽입
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모 > 자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p >= 1 and h[p] < h[c]:   # 부모가 있는데, 더 작으면 / 제 자리를 찾거나, 루트 노드가 될 때까지
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c//2


def deq():  # 삭제 / 마지막 노드 값을 복사 -> 마지막 노드 삭제 -> 자리를 찾는다
    global last
    tmp = h[1]   # 루트의 키값 보관
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2
    while c <= last:  # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]: # 오른쪽자식이 있고 오른쪽자식이 왼쪽자식보다 크면
            c += 1  # child index
        if h[p] < h[c]:  # 더 큰 자식노드를 구하고 부모노드와 비교
            h[p], h[c] = h[c], h[p]  # 자식노드가 더 크므로 부모노드와 자식노드 둘이 위치 변경

            p = c
            c = p*2
        else:  # 제 자리를 찾으면
            break
    return tmp  # 루트 키값 반환


N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

h = [0]*(N+1)   # 최대힙
last = 0        # 힙의 마지막 노드 번호

for num in arr:
    enq(num)

print(h)

while last > 0:
    print(deq(), end=' ')
