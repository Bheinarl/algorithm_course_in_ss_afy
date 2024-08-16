melon = int(input())

arr = [ [] for _ in range(5)]
lst = []
for _ in range(6):  # 동서남북 각자 길이
    n, m = map(int, input().split())
    lst += [[n,m]]
    arr[n] += [m]
    # arr : [[], [60, 100], [160], [30, 20], [50]]

lst += lst
# lst : [[4 50] [2 160] [3 30] [1 60] [3 20] [1 100] [4 50] [2 160] [3 30] [1 60] [3 20] [1 100]]

arr_i = []
for i in range(1,5):  # 전체 세로, 전체 가로 위치 인덱스 찾기
    if len(arr[i]) == 1:
        arr_i += [i]  # arr_i = [2, 4]

arr_j = []
for j in range(9):
    if lst[j][0] not in arr_i and lst[j+1][0] not in arr_i and lst[j+2][0] not in arr_i and lst[j+3][0] not in arr_i:
        arr_j += lst[j:j+4]

area = arr[arr_i[0]][0] * arr[arr_i[1]][0] - arr_j[1][1] * arr_j[2][1]

result = area * melon
print(result)