n = int(input())

for _ in range(n):
    termo = int(input())
    an = 1 * (2**termo)
    print(f"{an//12000} kg")