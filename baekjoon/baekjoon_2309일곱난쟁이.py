def f():
    for i in range(8):
        for j in range(i, 9):
            if ARR[i] + ARR[j] == over_num:
                ARR[i] = 0
                ARR[j] = 0
                ARR.remove(0)
                ARR.remove(0)
                return

            if ARR[i] + ARR[-1] < over_num:
                break

            if ARR[i] + ARR[j] > over_num:
                break


ARR = []
for _ in range(9):
    ARR += [int(input())]

ARR.sort()

over_num = sum(ARR) - 100

f()

for k in range(7):
    print(ARR[k])
