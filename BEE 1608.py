t = int(input())

for case in range(t):
    d, i, b = map(int, input().split())
    preco_ingredientes = list(map(int, input().split()))

    max_bolos = 0

    for _ in range(b):
        ingredientes = list(map(int, input().split()))

        custo_bolo = 0
        for j in range(ingredientes[0]):
            ingrediente_index = ingredientes[(j*2) + 1]
            ingrediente_quantitade = ingredientes[(j*2) + 2]
            preco_ingrediente = preco_ingredientes[ingrediente_index]
            custo_bolo += preco_ingrediente * ingrediente_quantitade

        quantidade_bolos = d // custo_bolo
        max_bolos = max(max_bolos, quantidade_bolos)
    print(max_bolos)
            


        