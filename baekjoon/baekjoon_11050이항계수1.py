def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)


N, K = map(int, input().split())

print( fac(N) // (fac(N-K) * fac(K)))