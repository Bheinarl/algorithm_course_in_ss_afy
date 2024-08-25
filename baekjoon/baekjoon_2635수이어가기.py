n1 = int(input())
max_counts = 0
max_num = 0


def f(num1, num2):
    counts = 0
    global max_counts
    global max_num
    while num2 >= 0:
        num1, num2 = num2, num1 - num2
        counts += 1

    if max_counts < counts:
        max_counts = counts
        max_num = i

    return


for i in range(1, n1+1):
    n2 = i
    f(n1, n2)

arr = [0] * (max_counts+1)
arr[0] = n1
arr[1] = max_num
n2 = max_num
for i in range(2, max_counts+1):
    arr[i] = n1 - n2
    n1, n2 = n2, n1 - n2

print(max_counts+1)
print(*arr)