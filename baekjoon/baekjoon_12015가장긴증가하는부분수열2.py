def ebuntamsec(arr, num):
    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if arr[mid_index] >= num:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return left_index

N = int(input())
LST = list(map(int, input().split()))

suyeol = []

for n in LST:
    index = ebuntamsec(suyeol, n)
    if index == len(suyeol):
        suyeol.append(n)
    else:
        suyeol[index] = n

print(len(suyeol))