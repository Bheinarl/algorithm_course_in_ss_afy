def f(n):

    month = N[4:6]
    date = N[6:]

    if int(month) in date_31:
        if 1 <= int(date) <= 31:
            return n
        else:
            return -1
    elif int(month) in date_30:
        if 1 <= int(date) <= 30:
            return n
        else:
            return -1
    elif int(month) == 2:
        if 1 <= int(date) <= 28:
            return n
        else:
            return -1
    else:
        return -1


T = int(input())

date_31 = [1, 3, 5, 7, 8, 10, 12]
date_30 = [4, 6, 9, 11]
date_28 = [2]

for t in range(1, T+1):
    N = str(input())

    ans = f(N)

    if ans == -1:
        print(f'#{t} {ans}')
    else:
        year = N[:4]
        month = N[4:6]
        date = N[6:]
        print(f'#{t} {year}/{month}/{date}')
