def f(month, sum_price):
    global min_price
    if month > 12:  # 12개월 넘으면 정산
        if min_price > sum_price:
            min_price = sum_price
    else:
        f(month+1, sum_price + ARR[month-1] * day)  # 이번 달은 1일 이용권으로
        f(month+1, sum_price + mon1)  # 이번 달은 1달 이용권으로
        f(month+3, sum_price + mon3)  # 이번 달은 3달 이용권으로


T = int(input())
for TEST_CASE in range(1, T+1):
    day, mon1, mon3, year = map(int, input().split())
    ARR = list(map(int, input().split()))
    min_price = 3000*365
    f(1, 0)
    min_price = min(min_price, year)

    print(f'#{TEST_CASE} {min_price}')
