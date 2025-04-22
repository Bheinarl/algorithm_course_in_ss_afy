def calculate_time(cow_list, heater_position):
    max_time = 0
    for i in range(len(cow_list)):
        heat_time = abs(i - heater_position) * cow_list[i]
        if heat_time > max_time:
            max_time = heat_time
    return max_time


N = int(input())
A = list(map(int, input().split()))

left = 0
right = N - 1
while right - left >= 3:
    m1 = left + (right - left) // 3
    m2 = right - (right - left) // 3
    m1_time = calculate_time(A, m1)
    m2_time = calculate_time(A, m2)
    if m1_time > m2_time:
        left = m1 + 1
    else:
        right = m2 - 1

ans = min(calculate_time(A, left), calculate_time(A, right), calculate_time(A, (left + right) // 2))
print(ans)