lis = [float(aux) for aux in input().split()]
a = max(lis)
lis.remove(a)
b = lis[0]
c = lis[1]
if a >= (b + c):
    print(f"NAO FORMA TRIANGULO")
else:
    if (a**2) == (b**2 + c**2):
        print(f"TRIANGULO RETANGULO")
    if (a**2) > (b**2 + c**2):
        print(f"TRIANGULO OBTUSANGULO")
    if (a**2) < (b**2 + c**2):
        print(f"TRIANGULO ACUTANGULO")
    if (a == b) and (a == c):
        print(f"TRIANGULO EQUILATERO")
    if (a == b and a != c) or (a != b and a == c) or (b == c and b != a):
        print(f"TRIANGULO ISOSCELES")