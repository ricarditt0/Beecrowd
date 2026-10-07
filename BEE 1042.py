a,b,c = map(int, input().split())

lista = []
lista.append(a)
lista.append(b)
lista.append(c)

lista.sort()
for n in lista:
    print(n)
print('')
print(a)
print(b)
print(c)