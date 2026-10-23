from itertools import combinations

def distancia_euclidiana(a, b):
    ax, ay = a
    bx, by = b
    return ((bx - ax) ** 2 + (by - ay))


n = int(input())

while n:
    pontos = []
    for _ in range(n):
        x,y = map(int, input().split())
        pontos.append((x, y))

    count = 0
    distacias = [0] * n
    for i in range(n):
        for j in range(n):
            distacias[j] = distancia_euclidiana(pontos[i],pontos[j])
        distacias.sort()
        k = 1
        for j in range(1,n):
            if distacias[j] == distacias[j-1]:
                k += 1
            else:
                count += (k*(k-1))//2
        count += (k*(k-1))//2

    print(count)
    n = int(input())