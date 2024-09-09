from collections import deque

def f(idx, lst_A, lst_B):

    global min_diff

    if min_diff == 0:  # 최소가 0이면 계속 할 의미가 없으니깐 그만해
        return

    if idx == N+1:
        T_F = 0
        T_F += check_list(lst_A)  # 다 연결 되어있으면 1, 아니면 0
        T_F += check_list(lst_B)  # 다 연결 되어있으면 1, 아니면 0
        if T_F == 2:  # 둘 다 오케이라면 최소를 구하자
            sum_A = 0
            for a in range(len(lst_A)):
                sum_A += people[lst_A[a]]

            sum_B = 0
            for b in range(len(lst_B)):
                sum_B += people[lst_B[b]]

            diff = abs(sum_A - sum_B)
            if min_diff > diff:
                min_diff = diff

        else:
            return -1
    else:  # 어떻게 나눌껀지 정해
        f(idx + 1, lst_A + [idx], lst_B)
        f(idx + 1, lst_A, lst_B + [idx])


def check_list(lst):

    # 적어도 하나는 있어야 한대 없으면 걸러
    if lst == []:
        return 0

    q = deque()
    q. append(lst[0])  # 맨 앞에있는거부터 시작해서 결국 전체를 다 돌면 되는것이야
    visited = set()
    visited.add(lst[0])  # 어느 노드를 갔는지 표시를 할꺼야

    while q:  # 경로를 다 스캔해봅시다.
        num = q.popleft()
        visited.add(num)
        if len(visited) == len(lst):  # 근데 가야할 곳과 간 곳이 같으면 끝 정상입니다.
            return 1


        for j in range(len(section[num])):  # 길을 순회하면서
            if section[num][j] in lst and section[num][j] not in visited:  # 앞으로 갈 길이 가야하는 노드거나, 방문한 적이 없는 곳이라면
                q.append(section[num][j])  # 길 저장하고
                visited.add(section[num][j])  # 갔다고 저장하고

    return 0


N = int(input())
people = [0] + list(map(int,input().split()))
section = [0]
for _ in range(N):
    temp = list(map(int, input().split()))
    temp = temp[1:]
    section.append(temp)
min_diff = N * 100+1
f(1, [], [])
if min_diff == N * 100 + 1:
    min_diff = -1

print(min_diff)
