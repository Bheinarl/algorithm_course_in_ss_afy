T = int(input())
for TEST_CASE in range(1, T+1):
    num2 = list(input())
    num3 = list(input())

    N2 = len(num2)
    N3 = len(num3)

    i = N2 - 1
    n2 = 0
    sum2 = 0
    while i >= 0:
        sum2 += int(num2[i]) * (2**n2)
        i -= 1
        n2 += 1

    j = N3 - 1
    n3 = 0
    sum3 = 0
    while j >= 0:
        sum3 += int(num3[j]) * (3**n3)
        j -= 1
        n3 += 1

    diff = abs(sum3 - sum2)

    lst2 = [2**n for n in range(N2)]
    lst3 = [3**n for n in range(N3)]

    for p in range(N2):
        for q in range(N3):
            if diff == lst2[p] + lst3[q]:
