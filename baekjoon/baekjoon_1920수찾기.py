N = int(input())
arr_A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

arr_A.sort()

for i in range(M):
    s = 0
    e = N-1
    while s <= e:
        mid = (s + e) // 2
        if arr[i] == arr_A[mid]:
            print(1)
            break
        elif arr[i] > arr_A[mid]:
            s = mid + 1
        elif arr[i] < arr_A[mid]:
            e = mid - 1

    if s > e:
        print(0)
