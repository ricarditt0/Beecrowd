def fatorail(n):
    if n == 0:
        return 1
    else:
        return n * fatorail(n - 1)

a = int(input())
print(fatorail(a))