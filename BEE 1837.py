a ,b = map(int, input().split())

r = a % abs(b)
q = (a - r) // b

print(f"{q} {r}")