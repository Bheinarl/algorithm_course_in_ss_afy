K = int(input())
ARR = [0, 0] + list(map(int, input().split()))

sum_list = [0] * 2**(K + 1)  # sum_list 는 리프노트부터 자기 index 까지의 노드 합 기록
for p in range(2**K, 2**(K+1)):  # 리프 노드들은 수기로 저장
    sum_list[p] = ARR[p]

for i in range(2 ** K - 1, 1, -1):  # 반대로 뒤(맨 아래)에서부터 순회
    # 본인 노드와 아래 가장 큰 합을 더한다.
    # 즉 발생할 수 있는 가장 큰 노드들의 합을 구한다.
    sum_list[i] += ARR[i] + max(sum_list[2 * i], sum_list[2 * i + 1])

for j in range(1, 2**K):  # 이번엔 앞(맨 위)에서부터 순회
    sum_left = sum_list[2 * j]
    sum_right = sum_list[2 * j + 1]
    if sum_left <= sum_right:  # 비교해서 차이만큼 원본 트리에 저장한다.
        ARR[2 * j] += sum_right - sum_left
    else:
        ARR[2 * j + 1] += sum_left - sum_right

print(sum(ARR))  # 0번과 1번 인덱스는 0이므로 계산에는 지장 X
