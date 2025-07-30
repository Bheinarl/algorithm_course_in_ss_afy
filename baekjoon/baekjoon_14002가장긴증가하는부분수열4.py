# def ebuntamsec(arr, num):
#     left_index = 0
#     right_index = len(arr) - 1
#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         if arr[mid_index] >= num:
#             right_index = mid_index - 1
#         else:
#             left_index = mid_index + 1
#     return left_index
#
#
# N = int(input())
# LST = list(map(int, input().split()))
#
# suyeol = []
# index_lst = [0] * N  # 각 수가 들어간 위치 기록
# trace = [-1] * N  # 인덱스로 수열 역추적
#
# for i in range(N):
#     num = LST[i]
#     idx = ebuntamsec(suyeol, num)
#
#     if idx == len(suyeol):
#         suyeol.append(num)  # 수열 끝에 num을 추가 -> 수열 길이 증가
#     else:
#         suyeol[idx] = num  # 기존 수를 num으로 대체 -> 수열 길이 동일
#
#     index_lst[i] = idx  # 현재 숫자가 어느 위치에 들어갔는지
#
#     # trace 배열 구성 (역추적용)
#     if idx > 0:
#         for j in range(i - 1, -1, -1):
#             if index_lst[j] == idx - 1 and LST[j] < LST[i]:
#                 trace[i] = j
#                 break
#
# print(len(suyeol))
#
# # 인덱스로 수열 역추적
# lis_index = index_lst.index(len(suyeol) - 1)
# result = []
# while lis_index != -1:
#     result.append(LST[lis_index])
#     lis_index = trace[lis_index]
#
# print(*reversed(result))


N = int(input())
LST = list(map(int, input().split()))

dp = [1] * N
index4backtracking = [-1] * N # 역추적용 인덱스

for i in range(N):
    for j in range(i):
        if LST[j] < LST[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            index4backtracking[i] = j

max_len = max(dp)
last_index = dp.index(max_len)

result = []
while last_index != -1:
    result.append(LST[last_index])
    last_index = index4backtracking[last_index]

print(max_len)
print(*reversed(result))
