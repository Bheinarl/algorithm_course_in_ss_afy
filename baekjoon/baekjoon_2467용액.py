import sys

N = int(sys.stdin.readline())
LST = list(map(int, sys.stdin.readline().split()))
min_diff_0 = 2000000000

for i in range(N-1):
    first_liquid = LST[i]

    start_index = i + 1
    final_index = N - 1

    while start_index <= final_index:
        if min_diff_0 == 0:
            break

        mid = (start_index + final_index) // 2
        mixed_liquid = first_liquid + LST[mid]

        if abs(mixed_liquid) < min_diff_0:
            min_diff_0 = abs(mixed_liquid)
            result1 = first_liquid
            result2 = LST[mid]

        if mixed_liquid < 0:
            start_index = mid + 1
        else:
            final_index = mid - 1

print(result1, result2)