n = int(input())
while n:
    encontrado = False
    m = 0
    while not encontrado:
        regioes = list(range(2,n+1))
        m += 1
        index = 0
        while len(regioes) > 1:
            index = (index + (m-1)) % len(regioes)
            regioes.pop(index)
        if regioes[0] == 13:
            encontrado = True
            regioes.clear()
            print(m)
    n = int(input())
 