def f():
    counts = 0
    for i in range(len(arr)):
        if counts == 0 and arr[i] == ')':
            return 'NO'
        elif arr[i] == '(':
            counts += 1
        elif arr[i] == ')':
            counts -= 1
    else:
        if counts != 0:
            return 'NO'
        else:
            return 'YES'


N = int(input())

for _ in range(N):
    arr = input()
    result = f()

    print(result)
