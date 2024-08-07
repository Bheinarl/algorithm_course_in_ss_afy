arr = []
num = str(input())

for n in range(len(num)):
    num = int(num)
    arr += [num % 10]
    num = num // 10

sum_num = 0

for number in arr:
    sum_num += number
print(sum_num)
