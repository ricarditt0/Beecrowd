n = int(input())

while n:
    pontos = []
    for _ in range(n):
        x,y = map(int, input().split())
        pontos.append((x, y))

    resposta = 0

    for i in range(n):
        distancias = []
        x1, y1 = pontos[i]

        for j in range(n):
            if i == j:
                continue
            x2,y2 = pontos[j]

            d = (x2 - x1)**2 +(y2 - y1)**2
            distancias.append(d)
        distancias.sort()
        k = 1
        for j in range(1, len(distancias)):
            if distancias[j] == distancias[j - 1]:
                k += 1
            else:
                resposta += k * (k - 1) // 2
                k = 1

        resposta += k * (k - 1) // 2

    print(resposta)

    n = int(input())