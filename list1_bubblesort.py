"""
def BubbleSort(a, N):  # 정렬할 list, N(원소 수)
    for i in range(N - 1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):  # 비교할 왼쪽 원소
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [7, 55, 78, 12, 42]
N = 5

BubbleSort(a, N)
print(a)
"""

N = 6
arr = [7, 2, 5, 3, 4, 1]

for i in range(N-1, 0, -1): # 각 구간의 끝 인덱스 i
    for j in range(i): # 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
        if arr[j] > arr[j+1]: # 왼쪽 원소가 더 크면 교환
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)