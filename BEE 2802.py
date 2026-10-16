def fat(n):
    i = n
    aux = 1
    while i != 0:
        aux = i * aux
        i = i - 1
    return aux

def comb(n,p):
    if n < p:
        return 0
    return fat(n)//(fat(p)*fat(n-p))

n = int(input())

regioes = 1 + comb(n,2) + comb(n,4)
print(int(regioes))